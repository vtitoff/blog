import typing as tp
from aiohttp import web
from app.context import AppContext


async def handle(_: web.Request, context: AppContext) -> web.Response:
    return web.json_response({"result": "Server is ok"})
