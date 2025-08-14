from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from django.contrib.auth.models import Group, Permission
from . import models
from . import serializers
from . import filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated] # Proteja seus endpoints
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = filters.UserFilter
    ordering_fields = ['id', 'name', 'username', 'email']
    ordering = ['-id']

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = filters.GroupFilter
    ordering_fields = '__all__'
    ordering = ['name']

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [OrderingFilter] # Apenas ordenação para permissões
    ordering_fields = ['id', 'name', 'codename']
    ordering = ['id']

class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = models.UserGroup.objects.all()
    serializer_class = serializers.UserGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = filters.UserGroupFilter
    ordering_fields = '__all__'
    ordering = ['-id']