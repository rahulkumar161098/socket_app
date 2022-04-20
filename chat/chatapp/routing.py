import imp
from django.urls import path
from . import consumers

websocket_pattrens=[
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
]