from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('permissions', views.PermissionViewSet)
router.register('user-groups', views.UserGroupViewSet)

urlpatterns = router.urls