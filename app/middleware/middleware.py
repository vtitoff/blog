from aiohttp import web

@web.middleware
async def test_middleware(request, handler):
    print('Middleware test called')
    response = await handler(request)
    print('Middleware after request called')
    return response