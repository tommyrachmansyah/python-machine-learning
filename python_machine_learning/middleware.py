from aiohttp import web

import json

@web.middleware
async def python_machine_learning_middleware(request, handler):
    if request.path == '/ping':
        return web.Response(text='PONG')
    result = await handler(request)
    return web.json_response(result)