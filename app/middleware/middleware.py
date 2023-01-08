from aiohttp import web


@web.middleware
async def basic_middleware(request, handler):
    print(request)
    response = await handler(request)
    return response
