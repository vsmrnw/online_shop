import os
from django.conf import settings
from conf.settings.base import CELERY_BROKER_URL
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

app = Celery('application', broker=CELERY_BROKER_URL)
CELERY_TIMEZONE = 'UTC'

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)