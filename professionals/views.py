from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from professionals import models, serializers, filters


class HealthProfessionalViewSet(viewsets.ModelViewSet):
    queryset = models.HealthProfessional.objects.all()
    serializer_class = serializers.HealthProfessionalSerializer
    filter_class = filters.HealthProfessionalFilter
    ordering_fields = '__all__'
    ordering = ['created_at']

    @action(detail=True, methods=['get'], url_path='history')
    def get_history(self, request, pk=None):
        """
        Returns the change history.
        """
        health_professional = self.get_object()
        history = health_professional.history.all()
        serializer = serializers.HistoricalHealthProfessionalSerializer(history, many=True)
        return Response(serializer.data)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    filter_class = filters.ScheduleFilter
    ordering_fields = '__all__'
    ordering = ['created_at']
