import os
from celery import Celery
from django.conf import settings


# Set default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "course_management_system.settings")

app = Celery(
    "course_management_system",
    backend=settings.CELERY_RESULT_BACKEND,
    broker=settings.CELERY_BROKER_URL,
)
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
