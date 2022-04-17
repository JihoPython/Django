from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(
        r'ws/chat/(?P<room_name>\w+)/$',
        consumers.ChatConsumer.as_asgi()
        # asgi application으로 등록하려면 as_asgi chaining 필요
    ),
]
