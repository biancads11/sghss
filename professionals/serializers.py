from professionals import models
from rest_framework import serializers


class HealthProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HealthProfessional
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HealthProfessional
        fields = '__all__'
