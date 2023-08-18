# myapp/tasks.py

from celery import shared_task

from .models import Drones
from .models import DronesBatteryHistory


@shared_task
def check_drones_battery():
    drone_query_set = Drones.objects.all()
    for drone in drone_query_set:
        try:
            history = DronesBatteryHistory(drone_id=drone, battery=drone.battery)
            history.save()
        except Exception as e:
            print(e)


check_drones_battery.apply_async(countdown=1, repeat=True)
