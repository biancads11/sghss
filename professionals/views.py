from rest_framework import viewsets
from professionals.filters import HealthProfessionalFilter, ScheduleFilter
from professionals.models import HealthProfessional, Schedule
from professionals.serializers import HealthProfessionalSerializer, ScheduleSerializer


class HealthProfessionalViewSet(viewsets.ModelViewSet):
    queryset = HealthProfessional.objects.all()
    serializer_class = HealthProfessionalSerializer
    filter_class = HealthProfessionalFilter
    ordering_fields = '__all__'
    ordering = ['created_at']

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_class = ScheduleFilter
    ordering_fields = '__all__'
    ordering = ['created_at']