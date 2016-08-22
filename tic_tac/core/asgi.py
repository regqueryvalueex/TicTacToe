"""
WSGI config for profit_reporter light_it.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangolight_it.com/en/1.8/howto/deployment/wsgi/
"""

import os
from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")

channel_layer = get_channel_layer()
