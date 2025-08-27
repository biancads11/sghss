from core.views import BaseViewSet
from professionals import models, serializers, filters


class HealthProfessionalViewSet(BaseViewSet):
    queryset = models.HealthProfessional.objects.all()
    serializer_class = serializers.HealthProfessionalSerializer
    filter_class = filters.HealthProfessionalFilter
    ordering_fields = '__all__'


class ScheduleViewSet(BaseViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    filter_class = filters.ScheduleFilter
    ordering_fields = '__all__'
