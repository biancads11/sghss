from django.contrib.auth.models import Group

from core.views import BaseViewSet
from infrastructure import serializers, filters


class HospitalUnitViewSet(BaseViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.HospitalUnitSerializer
    filterset_class = filters.HospitalUnitFilter
    ordering_fields = '__all__'
