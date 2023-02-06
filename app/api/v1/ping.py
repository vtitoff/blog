import typing as tp
from aiohttp import web
from app.context import AppContext


async def handle(context: AppContext, _: web.Request) -> web.Response:
    return web.json_response({"result": "Server is ok"})
