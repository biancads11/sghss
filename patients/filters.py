from django_filters import rest_framework as filters
from .models import Patient, MedicalRecord

ICONTAINS = 'icontains'

class PatientFilter(filters.FilterSet):
    # Permite buscar por qualquer parte do nome ou do CPF
    name = filters.CharFilter(field_name='name', lookup_expr=ICONTAINS)
    cpf = filters.CharFilter(field_name='cpf', lookup_expr=ICONTAINS)

    class Meta:
        model = Patient
        fields = ['name', 'cpf', 'gender']

class MedicalRecordFilter(filters.FilterSet):
    # Permite filtrar prontuários pelo ID do paciente
    patient = filters.NumberFilter(field_name='patient__id')

    class Meta:
        model = MedicalRecord
        fields = ['patient']