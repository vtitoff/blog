import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import users as users_utils
from app.constants import USERS_PER_PAGE
from app.utils.query_validator import LimitQueryValidator, PageQueryValidator


async def handle(context: AppContext, req: web.Request) -> web.Response:
    page = PageQueryValidator.get_int(req.rel_url.query.get("page", "0"))
    page_limit = LimitQueryValidator.get_int(
        req.rel_url.query.get("limit", USERS_PER_PAGE)
    )
    users, total_count = await users_utils.fetchall(
        context, page=page, page_limit=page_limit
    )
    return web.json_response(
        {
            "result": {
                "count": total_count,
                "users": [to_response(user) for user in users],
            }
        },
        headers={"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "content-type"}
    )


async def options_handle(req: web.Request, context: AppContext) -> web.Response:
    return web.json_response(
        headers={"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "content-type"}
    )


def to_response(user: models.User) -> dict:
    return {
        "login": user.login,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "user_info": user.user_info,
        "contacts": user.contacts,
    }
