from rest_framework import viewsets

from professionals import models, serializers, filters


class HealthProfessionalViewSet(viewsets.ModelViewSet):
    queryset = models.HealthProfessional.objects.all()
    serializer_class = serializers.HealthProfessionalSerializer
    filter_class = filters.HealthProfessionalFilter
    ordering_fields = '__all__'
    ordering = ['created_at']


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    filter_class = filters.ScheduleFilter
    ordering_fields = '__all__'
    ordering = ['created_at']
