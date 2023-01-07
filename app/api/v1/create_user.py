import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import users as users_utils


async def handle(req: web.Request, context: AppContext) -> web.Response:
    request_body = await req.json()
    user_services = []
    for service in request_body["services"]:
        try:
            user_services.append(models.Service.from_request(service))
        except KeyError:
            return web.json_response({"error": "key error!"}, status=400)
    user = await users_utils.create_user(
        context,
        login=request_body["login"],
        first_name=request_body["first_name"],
        last_name=request_body["last_name"],
        user_info=request_body["user_info"],
        services=user_services,
    )
    return web.json_response(
        {
            "result": [to_response(user)],
        }
    )


def to_response(user: models.User) -> dict:
    return {
        "user": {
            "login": user.login,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_info": user.user_info,
            "services": [
                {
                    "service_name": service.name,
                    "service_cost": service.cost,
                    "service_currency": service.currency,
                }
                for service in user.services
            ],
        }
    }
