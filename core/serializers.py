from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        # Exclui a senha por segurança. Crie um endpoint separado para alteração de senha.
        exclude = ('password',)

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class UserGroupSerializer(serializers.ModelSerializer):
    # Inclui a representação em string do grupo para melhor visualização
    group_name = serializers.CharField(source='group.name', read_only=True)

    class Meta:
        model = models.UserGroup
        fields = ['id', 'user', 'group', 'group_name']