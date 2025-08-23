from django_filters import rest_framework as filters
from clinical_service import models

class AppointmentFilter(filters.FilterSet):
    patient = filters.NumberFilter(field_name='patient__id')
    professional = filters.NumberFilter(field_name='professional__id')
    start_date = filters.DateFilter(field_name='timestamp__date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='timestamp__date', lookup_expr='lte')

    class Meta:
        model = models.Appointment
        fields = ['patient', 'professional', 'appointment_type', 'status', 'start_date', 'end_date']


class ConsultationFilter(filters.FilterSet):
    appointment = filters.NumberFilter(field_name='appointment__id')

    class Meta:
        model = models.Consultation
        fields = ['appointment', 'specialty', 'status']


class ExaminationFilter(filters.FilterSet):
    patient = filters.NumberFilter(field_name='patient__id')
    requesting_professional = filters.NumberFilter(field_name='requesting_professional__id')
    request_date = filters.DateFilter(field_name='request_date')

    class Meta:
        model = models.Examination
        fields = ['patient', 'requesting_professional', 'exam_type', 'request_date']


class PrescriptionFilter(filters.FilterSet):
    appointment = filters.NumberFilter(field_name='appointment__id')
    professional = filters.NumberFilter(field_name='professional__id')

    class Meta:
        model = models.Prescription
        fields = ['appointment', 'professional']