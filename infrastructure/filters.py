from django_filters import rest_framework as filters
from infrastructure import models

ICONTAINS = 'icontains'


class HospitalUnitFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr=ICONTAINS)
    unit_type = filters.CharFilter(field_name='unit_type', lookup_expr=ICONTAINS)
    address = filters.CharFilter(field_name='address', lookup_expr=ICONTAINS)

    class Meta:
        model = models.HospitalUnit
        fields = ['name', 'unit_type', 'address']
