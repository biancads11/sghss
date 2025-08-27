from core.views import BaseViewSet
from patients import models, serializers, filters


class PatientViewSet(BaseViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    filterset_class = filters.PatientFilter
    ordering_fields = ['__all__']


class MedicalRecordViewSet(BaseViewSet):
    queryset = models.MedicalRecord.objects.all()
    serializer_class = serializers.MedicalRecordSerializer
    filterset_class = filters.MedicalRecordFilter
    ordering_fields = ['__all__']
