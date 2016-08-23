from rest_framework import generics, permissions
from games import models
from . import serializers


class RetrieveGameAPI(generics.RetrieveAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    permission_classes = permissions.AllowAny,
