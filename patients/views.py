from rest_framework import viewsets
from .filters import PatientFilter, MedicalRecordFilter
from .models import Patient, MedicalRecord
from .serializers import PatientSerializer, MedicalRecordSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_class = PatientFilter
    ordering_fields = '__all__'
    ordering = ['created_at']


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    filterset_class = MedicalRecordFilter
    ordering_fields = '__all__'
    ordering = ['created_at']