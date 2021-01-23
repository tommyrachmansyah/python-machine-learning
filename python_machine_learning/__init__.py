from aiohttp import web
from python_machine_learning.middleware import python_machine_learning_middleware
from python_machine_learning.routes import all_routes

import logging
import settings

logging.basicConfig(
    format='%(asctime)s:%(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)

app = web.Application(middlewares=[python_machine_learning_middleware])
app.add_routes(all_routes)

def run_server():
    connection_args = {
        "host": settings.SERVER_HOST,
        "port": settings.SERVER_PORT
    }
    logging.info('App run!')
    web.run_app(app=app, **connection_args)