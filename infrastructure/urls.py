from rest_framework.routers import DefaultRouter

from infrastructure import views

router = DefaultRouter()
router.register('hospital_unit', views.HospitalUnitViewSet)

urlpatterns = router.urls
