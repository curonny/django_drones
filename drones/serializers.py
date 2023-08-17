from rest_framework import serializers

from .models import Drones
from .models import Medication


class DronesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drones
        fields = '__all__'


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'
