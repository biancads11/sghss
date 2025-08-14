from django_filters import rest_framework as filters
from django.contrib.auth.models import Group, Permission
from . import models

ICONTAINS = 'icontains'

class UserFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr=ICONTAINS)
    username = filters.CharFilter(field_name='username', lookup_expr=ICONTAINS)
    email = filters.CharFilter(field_name='email', lookup_expr=ICONTAINS)

    class Meta:
        model = models.User
        fields = ['name', 'username', 'email']

class GroupFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr=ICONTAINS)

    class Meta:
        model = Group
        fields = ['name']

class UserGroupFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name='user__id')
    group = filters.NumberFilter(field_name='group__id')

    class Meta:
        model = models.UserGroup
        fields = ['user', 'group']