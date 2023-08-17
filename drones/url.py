from rest_framework import routers

from .api import DronesViewSet
from .api import MedicamentoFiltradoViewSet
from .api import MedicationLoadViewSet
from .api import MedicationViewSet

router = routers.DefaultRouter()

router.register('api/drones', DronesViewSet, 'drones')
router.register('api/medications', MedicationViewSet, 'medications')
router.register('api/medicationload', MedicationLoadViewSet, 'medicationload')
router.register(r'api/medicationload_filters', MedicamentoFiltradoViewSet,
                basename='medicationload_filters')

urlpatterns = router.urls
