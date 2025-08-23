from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, Permission
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from core import serializers, models, filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_class = filters.UserFilter
    ordering_fields = ['__all__']
    ordering = ['-id']

    @action(detail=False, methods=['POST'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)

            return Response({"token": str(refresh)}, status=status.HTTP_200_OK)
        return Response({"detail": "Usuário não encontrado"}, status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filterset_class = filters.GroupFilter
    ordering_fields = '__all__'
    ordering = ['name']


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
    ordering = ['id']


class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = models.UserGroup.objects.all()
    serializer_class = serializers.UserGroupSerializer
    filterset_class = filters.UserGroupFilter
    ordering_fields = '__all__'
    ordering = ['-id']
