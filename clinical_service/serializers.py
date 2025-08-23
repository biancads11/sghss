from rest_framework import serializers

from clinical_service import models


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consultation
        fields = '__all__'


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Examination
        fields = '__all__'


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prescription
        fields = '__all__'
