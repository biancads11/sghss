from django_filters import rest_framework as filters
from patients import models

ICONTAINS = 'icontains'


class PatientFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr=ICONTAINS)
    cpf = filters.CharFilter(field_name='cpf', lookup_expr=ICONTAINS)

    class Meta:
        model = models.Patient
        fields = ['name', 'cpf', 'gender']


class MedicalRecordFilter(filters.FilterSet):
    patient = filters.NumberFilter(field_name='patient__id')

    class Meta:
        model = models.MedicalRecord
        fields = ['patient']
