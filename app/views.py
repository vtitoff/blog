from aiohttp import web
import aiohttp_jinja2
import requests
from app.constants import HOST
from app.context import AppContext
from app.utils import users as users_utils



@aiohttp_jinja2.template("index.html")
async def index(ctx: AppContext, req: web.Request) -> dict:
    return {"title": "Blog"}


@aiohttp_jinja2.template("user.html")
async def user(ctx: AppContext, req: web.Request) -> dict:
    user, user_services = await users_utils.fetchone(ctx, req.match_info["login"])
    return {"user": user}
