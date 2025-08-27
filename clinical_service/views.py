from clinical_service import models, serializers, filters
from core.views import BaseViewSet


class AppointmentViewSet(BaseViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    filter_class = filters.AppointmentFilter
    ordering_fields = '__all__'


class ConsultationViewSet(BaseViewSet):
    queryset = models.Consultation.objects.all()
    serializer_class = serializers.ConsultationSerializer
    filter_class = filters.ConsultationFilter
    ordering_fields = '__all__'


class ExaminationViewSet(BaseViewSet):
    queryset = models.Examination.objects.all()
    serializer_class = serializers.ExaminationSerializer
    filter_class = filters.ExaminationFilter
    ordering_fields = '__all__'


class PrescriptionViewSet(BaseViewSet):
    queryset = models.Prescription.objects.all()
    serializer_class = serializers.PrescriptionSerializer
    filter_class = filters.PrescriptionFilter
    ordering_fields = '__all__'
