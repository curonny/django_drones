from rest_framework import routers

from .api import DroneToLoadingViewSet
from .api import DronesViewSet
from .api import MedicationByDroneIdViewSet
from .api import MedicationLoadViewSet
from .api import MedicationViewSet

router = routers.DefaultRouter()

router.register('api/drones', DronesViewSet, 'drones')
router.register('api/medications', MedicationViewSet, 'medications')
router.register('api/medicationload', MedicationLoadViewSet, 'medicationload')
router.register(r'api/medicationload_filters', MedicationByDroneIdViewSet,
                basename='medicationload_filters')
router.register(r'api/drones_to_loading', DroneToLoadingViewSet,
                basename='drones_to_loading')

urlpatterns = router.urls
