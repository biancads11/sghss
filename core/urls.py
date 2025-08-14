from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'permissions', views.PermissionViewSet)
router.register(r'user-groups', views.UserGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]