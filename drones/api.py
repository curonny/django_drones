from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Drones
from .models import Medication
from .models import MedicationLoad
from .serializers import DronesSerializer
from .serializers import MedicationLoadSerializer
from .serializers import MedicationSerializer


class DronesViewSet(viewsets.ModelViewSet):
    queryset = Drones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DronesSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicationSerializer


class MedicationLoadViewSet(viewsets.ModelViewSet):
    queryset = MedicationLoad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicationLoadSerializer


@action(detail=False, methods=['get'])
class MedicationByDroneIdViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MedicationSerializer

    def get_queryset(self):
        drone_id = self.request.query_params.get('drone_id')
        if drone_id is not None:
            queryset = MedicationLoad.objects.filter(drone_id=drone_id).values('medications')
            medication_ids = [item['medications'] for item in queryset]
            medications = Medication.objects.filter(id__in=medication_ids)
            return medications
        else:
            return []


@action(detail=False, methods=['get'])
class DroneToLoadingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DronesSerializer

    def get_queryset(self):
        queryset = Drones.objects.filter(battery__lt=25)
        return queryset
