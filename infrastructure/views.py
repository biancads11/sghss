from django.contrib.auth.models import Group
from rest_framework import viewsets

from infrastructure import serializers, filters


class HospitalUnitViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.HospitalUnitSerializer
    filterset_class = filters.HospitalUnitFilter
    ordering_fields = '__all__'
    ordering = ['name']
