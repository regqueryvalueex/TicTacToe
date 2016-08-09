from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')

from django.conf import settings

app = Celery('tasks')
app.config_from_object('celeryconfig')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()
