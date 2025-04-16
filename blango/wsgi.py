"""
WSGI config for blango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from blog.routing import websocket_urlpatterns 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blango.settings')
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

# from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()

# WebSocket support
application = ProtocolTypeRouter({
    "http": django_application,
    "websocket": URLRouter(
        websocket_urlpatterns  # From blog/routing.py
    ),
})