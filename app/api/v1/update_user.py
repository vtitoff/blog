import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import users as users_utils


async def handle(ctx: AppContext, req: web.Request) -> web.Response:
    request_body = await req.json()
    if not request_body.get("login"):
        return web.json_response({"error": "login not specified!"}, status=400)
    user = await users_utils.update_user(
        ctx,
        **request_body,
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
            "contacts": user.contacts,
        }
    }
