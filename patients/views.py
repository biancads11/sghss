from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from patients import models, serializers, filters


class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    filter_class = filters.PatientFilter
    ordering_fields = '__all__'
    ordering = ['created_at']

    @action(detail=True, methods=['get'], url_path='history')
    def get_history(self, request, pk=None):
        """
        Returns the change history.
        """
        patient = self.get_object()
        history = patient.history.all()
        serializer = serializers.HistoricalPatientSerializer(history, many=True)
        return Response(serializer.data)


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = models.MedicalRecord.objects.all()
    serializer_class = serializers.MedicalRecordSerializer
    filterset_class = filters.MedicalRecordFilter
    ordering_fields = '__all__'
    ordering = ['created_at']
