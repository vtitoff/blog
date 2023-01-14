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
            "result": [service.title for service in services],
        }
    )
    # return web.json_response(
    #     {
    #         "result": to_response(services),
    #     }
    # )


# def to_response(user: models.Service) -> dict:
#     return {
#         "login": user.login,
#         "first_name": user.first_name,
#         "last_name": user.last_name,
#         "user_info": user.user_info,
#         "contacts": user.contacts,
#     }
