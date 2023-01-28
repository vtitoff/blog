import aiohttp_jinja2
import requests
from app.constants import HOST


@aiohttp_jinja2.template("index.html")
async def index(request):
    return {"title": "Blog"}


@aiohttp_jinja2.template("user.html")
async def user(request):
    login = request.match_info["login"]
    return {"user": login}
