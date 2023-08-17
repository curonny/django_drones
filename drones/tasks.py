# myapp/tasks.py

from celery import shared_task

from .models import Drones


@shared_task
def check_drones_battery():
    query_set = Drones.objects.all()
    print(query_set)
