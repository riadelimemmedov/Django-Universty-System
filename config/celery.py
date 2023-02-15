from __future__ import absolute_import,unicode_literals
import os
from time import timezone

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')


app = Celery('config')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Baku')

app.config_from_object(settings,namespace='CELERY')


app.conf.beat_schedule = {
    
}

app.autodiscover_tasks()