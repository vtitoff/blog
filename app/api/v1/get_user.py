import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import users as users_utils


async def handle(context: AppContext, req: web.Request) -> web.Response:
    user, user_services = await users_utils.fetchone(context, req.match_info["login"])
    if not user:
        return web.json_response(
            {
                "result": [],
            },
            status=404,
        )
    return web.json_response(
        {
            "result": to_response(user, user_services),
        }
    )


def to_response(user: models.User, user_services: tp.List[models.Service]) -> dict:
    return {
        "login": user.login,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "user_info": user.user_info,
        "contacts": user.contacts,
        "services": [service.to_dict(service) for service in user_services],
    }
