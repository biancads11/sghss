from django.contrib.auth.models import Group, Permission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from core import serializers, models, filters
from core.mixins import HistoryViewSetMixin


class BaseViewSet(viewsets.ModelViewSet, HistoryViewSetMixin):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['created_at']

    class Meta:
        abstract = True


class UserViewSet(BaseViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_class = filters.UserFilter
    ordering_fields = ['__all__']

    @action(detail=True, methods=['get'], url_path='history')
    def get_history(self, request, pk=None):
        user = self.get_object()
        history = user.history.all()
        serializer = serializers.HistoricalUserSerializer(history, many=True)
        return Response(serializer.data)


class GroupViewSet(BaseViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filterset_class = filters.GroupFilter
    ordering_fields = ['__all__']


class PermissionViewSet(BaseViewSet):
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
    ordering = ['id']


class UserGroupViewSet(BaseViewSet):
    queryset = models.UserGroup.objects.all()
    serializer_class = serializers.UserGroupSerializer
    filterset_class = filters.UserGroupFilter
    ordering_fields = ['__all__']
