from django.conf.urls import url
from .consumers import ACMEDataConsumer
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/device/', consumers.ACMEDataConsumer.as_asgi()),
]