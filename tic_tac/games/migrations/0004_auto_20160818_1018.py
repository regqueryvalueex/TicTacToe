# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20160809_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='aborted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='move',
            name='game',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
            preserve_default=False,
        ),
    ]