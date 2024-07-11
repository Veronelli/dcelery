import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTING_MODULE', 'dcelery.settings')
app = Celery('dcelery')

app.conf.from_object('django.conf:settings', namespace='Celery')

@app.task
def add_numbers() -> int:
    return 100 + 20
