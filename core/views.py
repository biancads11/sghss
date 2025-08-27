from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, Permission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.filters import OrderingFilter

from core import serializers, models, filters
from core.mixins import HistoryViewSetMixin


class BaseViewSet(viewsets.ModelViewSet, HistoryViewSetMixin):
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['created_at']

    class Meta:
        abstract = True


class UserViewSet(BaseViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_class = filters.UserFilter
    ordering_fields = ['__all__']

    # apagar action de login e usar endpoint de token para pegar os tokens
    @action(detail=False, methods=['POST'], permission_classes = [AllowAny])

    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)

            return Response({"token": str(refresh.access_token)}, status=status.HTTP_200_OK)
        return Response({"detail": "Usuário não encontrado"}, status=status.HTTP_400_BAD_REQUEST)

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
