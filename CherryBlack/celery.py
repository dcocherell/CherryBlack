from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CherryBlack.settings')

app = Celery('CherryBlack')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.task_send_sent_event = True
app.conf.worker_send_task_events = True

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
