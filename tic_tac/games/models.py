# coding=utf-8
import datetime

from django.contrib.postgres.fields import JSONField
from django.db import models


class Game(models.Model):

    finished = models.BooleanField(default=False)
    finished_time = models.DateTimeField(blank=True, null=True)
    aborted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField(verbose_name='Field size', default=3)
    min_length = models.IntegerField(verbose_name='Line length', default=3)
    allow_horizontal = models.BooleanField(default=True)
    allow_vertical = models.BooleanField(default=True)
    allow_diagonal = models.BooleanField(default=True)
    finish_line = JSONField(blank=True, default={})

    class Meta:
        verbose_name = u"Game"
        verbose_name_plural = u"Games"


class Move(models.Model):
    game = models.ForeignKey(Game)
    x = models.IntegerField()
    y = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"Move"
        verbose_name_plural = u"Moves"
        ordering = 'created',
