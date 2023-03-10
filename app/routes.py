from aiohttp import web
from app.api.v1 import (
    ping,
    get_users,
    create_user,
    get_user,
    update_user,
    delete_user,
    get_services_by_login,
)
from app.context import AppContext
from app import views


def wrap_handler(handler, context, request_parser=None):
    async def wrapper(request):
        if request_parser:
            try:
                request = await request_parser(request)
            except ValueError as exc:
                return web.json_response(
                    {"code": "request_error", "error": str(exc)}, status=400
                )
        return await handler(context, request)

    return wrapper


def setup_routes(app: web.Application, ctx: AppContext) -> None:
    app.router.add_get(
        "/api/v1/ping",
        wrap_handler(ping.handle, ctx),
    )
    app.router.add_get(
        "/api/v1/users/{login}",
        wrap_handler(get_user.handle, ctx),
    )
    app.router.add_get(
        "/api/v1/users",
        wrap_handler(get_users.handle, ctx),
    )
    app.router.add_options(
        "/api/v1/users",
        wrap_handler(get_users.options_handle, ctx),
    )
    app.router.add_post(
        "/api/v1/users",
        wrap_handler(create_user.handle, ctx),
    )
    app.router.add_patch(
        "/api/v1/users/{login}/update",
        wrap_handler(update_user.handle, ctx),
    )
    app.router.add_delete(
        "/api/v1/users/{login}/delete",
        wrap_handler(delete_user.handle, ctx),
    )
    app.router.add_get(
        "/api/v1/services/{login}",
        wrap_handler(get_services_by_login.handle, ctx),
    )
    app.router.add_get(
        "/",
        wrap_handler(views.index, ctx),
    )
    app.router.add_get(
        "/{login}",
        wrap_handler(views.user, ctx),
    )
    app.add_routes([web.static('/static', "static")])
