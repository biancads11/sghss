from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import Patient, MedicalRecord
from .serializers import PatientSerializer, MedicalRecordSerializer
from .filters import PatientFilter, MedicalRecordFilter


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Adicionando os backends de filtro e ordenação
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PatientFilter

    # Campos pelos quais a API pode ser ordenada
    ordering_fields = ['id', 'name', 'birth_date', 'created_at']
    # Ordenação padrão
    ordering = ['-created_at']


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MedicalRecordFilter
    ordering_fields = ['id', 'patient__name', 'created_at']
    ordering = ['-created_at']