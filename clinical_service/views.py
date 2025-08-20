from rest_framework import viewsets

from clinical_service.filters import AppointmentFilter, ConsultationFilter, ExaminationFilter, PrescriptionFilter
from clinical_service.models import Appointment, Consultation, Examination, Prescription
from clinical_service.serializers import AppointmentSerializer, ConsultationSerializer, ExaminationSerializer, \
    PrescriptionSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_class = AppointmentFilter
    ordering_fields = '__all__'
    ordering = ['created_at']

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    filter_class = ConsultationFilter
    ordering_fields = '__all__'
    ordering = ['created_at']

class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer
    filter_class = ExaminationFilter
    ordering_fields = '__all__'
    ordering = ['created_at']

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    filter_class = PrescriptionFilter
    ordering_fields = '__all__'
    ordering = ['created_at']