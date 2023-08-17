from rest_framework import serializers

from .models import Drones
from .models import Medication
from .models import MedicationLoad


class DronesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drones
        fields = '__all__'


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class MedicationLoadSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(many=True)

    class Meta:
        model = MedicationLoad
        fields = '__all__'


class MedicationsByDronIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationLoad
        fields = '__all__'
