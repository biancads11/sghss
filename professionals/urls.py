from rest_framework.routers import DefaultRouter

from professionals import views

router = DefaultRouter()
router.register('professional', views.HealthProfessionalViewSet)
router.register('schedule', views.ScheduleViewSet)

urlpatterns = router.urls