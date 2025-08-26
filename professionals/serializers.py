from professionals import models
from rest_framework import serializers


class HealthProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HealthProfessional
        fields = '__all__'


class HistoricalHealthProfessionalSerializer(serializers.ModelSerializer):
    history_user_name = serializers.CharField(source='history_user.name', read_only=True, default=None)

    class Meta:
        model = models.HealthProfessional.history.model
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HealthProfessional
        fields = '__all__'
