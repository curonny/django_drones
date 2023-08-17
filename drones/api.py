from rest_framework import viewsets, permissions

from .models import Drones
from .models import Medication
from .serializers import DronesSerializer
from .serializers import MedicationSerializer


class DronesViewSet(viewsets.ModelViewSet):
    queryset = Drones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DronesSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicationSerializer
