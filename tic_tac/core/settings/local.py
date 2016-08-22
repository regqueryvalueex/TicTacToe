from .base import *

INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar', )

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "core.routing.channel_routing",
    },
}
