import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import users as users_utils


async def handle(req: web.Request, context: AppContext) -> web.Response:
    user = await users_utils.delete_user(context, req.match_info["login"])
    if not user:
        return web.json_response(
            {
                "result": "",
            },
            status=404,
        )
    return web.json_response(
        {
            "result": {},
        },
        status=204,
    )
