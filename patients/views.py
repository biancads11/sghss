from rest_framework import viewsets

from patients import models, serializers, filters


class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    filter_class = filters.PatientFilter
    ordering_fields = '__all__'
    ordering = ['created_at']


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = models.MedicalRecord.objects.all()
    serializer_class = serializers.MedicalRecordSerializer
    filterset_class = filters.MedicalRecordFilter
    ordering_fields = '__all__'
    ordering = ['created_at']
