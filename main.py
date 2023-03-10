import argparse
import asyncio
import pathlib
import jinja2
import aiohttp_jinja2
from aiohttp import web
from app.context import AppContext
from app import routes
from app.middleware import middleware


def setup_external_libraries(application: web.Application) -> None:
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))


async def create_app(args):
    app = web.Application(middlewares=[middleware.basic_middleware])
    ctx = AppContext(secrets_dir=args.secrets_dir)
    app.on_startup.append(ctx.on_startup)
    app.on_shutdown.append(ctx.on_shutdown)
    setup_external_libraries(app)
    app['static_root_url'] = '/static'
    routes.setup_routes(app, ctx)
    return app


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--secrets-dir", type=pathlib.Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    app = asyncio.get_event_loop().run_until_complete(create_app(args))
    web.run_app(app)


if __name__ == "__main__":
    main()
