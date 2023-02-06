import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import services as service_utils


async def handle(context: AppContext, req: web.Request) -> web.Response:
    request_body = await req.json()
    service = await service_utils.create_user(
        context,
        name=request_body["title"],
        description=request_body["description"],
        cost=request_body["cost"],
        currency=request_body["currency"],
        user_login=request_body["user_login"],
    )
    return web.json_response(
        {
            "result": [to_response(service)],
        }
    )


def to_response(service: models.Service) -> dict:
    return {
        "service": {
            "id": service.id,
            "title": service.title,
            "description": service.description,
            "cost": service.cost,
            "currency": service.currency,
            "user_login": service.user_login,
        }
    }
