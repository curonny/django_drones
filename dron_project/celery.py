from celery import Celery

app = Celery('drones')

# Celery's config using project settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Check task in app apps
app.autodiscover_tasks()
