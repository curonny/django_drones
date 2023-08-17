from rest_framework import routers

from .api import DronesViewSet
from .api import MedicationViewSet

router = routers.DefaultRouter()

router.register('api/drones', DronesViewSet, 'drones')
router.register('api/medications', MedicationViewSet, 'medications')

urlpatterns = router.urls
