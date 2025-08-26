from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from core import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ('password',)


class HistoricalUserSerializer(serializers.ModelSerializer):
    history_user_name = serializers.CharField(source='history_user.name', read_only=True, default=None)

    class Meta:
        model = models.User.history.model
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
    group_name = serializers.CharField(source='group.name', read_only=True)

    class Meta:
        model = models.UserGroup
        fields = ['id', 'user', 'group', 'group_name']
