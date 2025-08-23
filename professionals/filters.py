from django_filters import rest_framework as filters
from professionals import models

ICONTAINS = 'icontains'


class HealthProfessionalFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr=ICONTAINS)
    specialty = filters.CharFilter(field_name='specialty', lookup_expr=ICONTAINS)

    class Meta:
        model = models.HealthProfessional
        fields = ['name', 'specialty', 'position']


class ScheduleFilter(filters.FilterSet):
    professional = filters.NumberFilter(field_name='professional__id')
    date = filters.DateFilter(field_name='date')
    is_available = filters.BooleanFilter(field_name='is_available')

    class Meta:
        model = models.Schedule
        fields = ['professional', 'date', 'is_available']
