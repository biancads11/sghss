from rest_framework import serializers
from .models import Patient, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    # Inclui o nome do paciente para melhor visualização
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = MedicalRecord
        fields = '__all__'