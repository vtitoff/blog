import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import users as users_utils


async def handle(context: AppContext, req: web.Request) -> web.Response:
    request_body = await req.json()
    user = await users_utils.create_user(
        context,
        login=request_body["login"],
        first_name=request_body["first_name"],
        last_name=request_body["last_name"],
        user_info=request_body["user_info"],
        contacts=request_body["contacts"],
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
