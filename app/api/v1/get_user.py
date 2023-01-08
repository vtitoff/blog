import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import users as users_utils


async def handle(req: web.Request, context: AppContext) -> web.Response:
    user = await users_utils.fetchone(context, req.match_info["login"])
    if not user:
        return web.json_response(
            {
                "result": "",
            },
            status=404,
        )
    return web.json_response(
        {
            "result": to_response(user),
        }
    )


def to_response(user: models.User) -> dict:
    return {
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
