from rest_framework import viewsets, permissions
from rest_framework.decorators import action

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

    # def perform_create(self, serializer):
    #     total_weight = sum(m.weight for m in serializer.validated_data.get('medications'))
    #     if total_weight > serializer.validated_data.get('drone_id').weight_limit:
    #         raise ValidationError({"error": " The total_weight is %s and the total medication weight is %s" % (
    #             serializer.validated_data.get('drone_id').weight_limit, total_weight)}, code=400)
    #
    #     serializer.save()


@action(detail=False, methods=['get'])
class MedicamentoFiltradoViewSet(viewsets.ReadOnlyModelViewSet):
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
