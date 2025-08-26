from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from clinical_service import models, serializers, filters


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    filter_class = filters.AppointmentFilter
    ordering_fields = '__all__'
    ordering = ['created_at']


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = models.Consultation.objects.all()
    serializer_class = serializers.ConsultationSerializer
    filter_class = filters.ConsultationFilter
    ordering_fields = '__all__'
    ordering = ['created_at']

    @action(detail=True, methods=['get'], url_path='history')
    def get_history(self, request, pk=None):
        """
        Returns the change history.
        """
        consultation = self.get_object()
        history = consultation.history.all()
        serializer = serializers.HistoricalConsultationSerializer(history, many=True)
        return Response(serializer.data)


class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = models.Examination.objects.all()
    serializer_class = serializers.ExaminationSerializer
    filter_class = filters.ExaminationFilter
    ordering_fields = '__all__'
    ordering = ['created_at']


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = models.Prescription.objects.all()
    serializer_class = serializers.PrescriptionSerializer
    filter_class = filters.PrescriptionFilter
    ordering_fields = '__all__'
    ordering = ['created_at']
