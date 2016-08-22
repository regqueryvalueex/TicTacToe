from django.contrib.auth import get_user_model
from rest_framework import serializers

from games import models


class MoveSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Move
        fields = 'x', 'y', 'created',


class GameSerializer(serializers.ModelSerializer):

    moves = MoveSerializer(many=True, read_only=True, source='move_set')

    class Meta:
        model = models.Game
        fields = 'id', 'finished', 'finished_time', 'aborted', 'created',\
                 'size', 'min_length', 'allow_horizontal', 'allow_vertical',\
                 'allow_diagonal', 'finish_line', 'moves',
