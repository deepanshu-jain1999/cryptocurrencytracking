import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptocurrency.settings')

app = Celery('cryptocurrency')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
