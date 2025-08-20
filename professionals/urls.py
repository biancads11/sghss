from rest_framework.routers import DefaultRouter

from professionals.views import HealthProfessionalViewSet, ScheduleViewSet

router = DefaultRouter()
router.register('professional', HealthProfessionalViewSet)
router.register('schedule', ScheduleViewSet)

urlpatterns = router.urls