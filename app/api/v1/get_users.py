import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import users as users_utils


async def handle(_: web.Request, context: AppContext) -> web.Response:
    users = await users_utils.fetchall(context)
    return web.json_response(
        {
            'users': [to_response(user) for user in users],
        }
    )


def to_response(user: models.User) -> dict:
    return {
        'login': user.login,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'user_info': user.user_info,
        'services': [{'service_name': service.name, 'service_cost': service.cost, 'service_currency': service.currency} for service in user.services]
    }
