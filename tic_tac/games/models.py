# coding=utf-8
import datetime

from django.db import models


class Game(models.Model):

    finished = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField(verbose_name='Field size', default=3)
    min_length = models.IntegerField(verbose_name='Line length', default=3)
    allow_horizontal = models.BooleanField(default=True)
    allow_vertical = models.BooleanField(default=True)
    allow_diagonal = models.BooleanField(default=True)

    class Meta:
        verbose_name = u"Game"
        verbose_name_plural = u"Games"


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"Move"
        verbose_name_plural = u"Moves"
        ordering = 'created',
