from rest_framework import serializers
from patients import models


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = models.MedicalRecord
        fields = '__all__'
