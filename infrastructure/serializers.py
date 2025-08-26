from rest_framework import serializers

from infrastructure import models


class HospitalUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HospitalUnit
        fields = '__all__'