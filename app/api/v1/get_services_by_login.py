import typing as tp
from aiohttp import web
from app.context import AppContext
from app import dto, models
from app.utils import services as service_utils


async def handle(req: web.Request, context: AppContext) -> web.Response:
    services = await service_utils.get_services_by_login(context, req.match_info["login"])
    if not services:
        return web.json_response(
            {
                "result": "",
            },
            status=404,
        )
    return web.json_response(
        {
            "result": [to_response(service) for service in services],
        }
    )


def to_response(service: models.Service) -> dict:
    return {
        "id": str(service.id),
        "title": service.title,
        "description": service.description,
        "cost": service.cost,
        "currency": service.currency,
        "user_login": service.user_login,
    }
