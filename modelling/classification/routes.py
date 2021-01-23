from aiohttp import web
from modelling.classification.models import Message

classification_route = [
  web.get('/message', Message.get_result)
]