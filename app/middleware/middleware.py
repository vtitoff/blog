from aiohttp import web
import datetime

@web.middleware
async def basic_middleware(request, handler):
    print(request)
    try:
        print(datetime.datetime.now())
        print(request.headers)
    except Exception as e:
        print(e)
    response = await handler(request)
    print("Response status is:")
    print(response.status)
    print('\n')
    return response
