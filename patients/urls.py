from rest_framework.routers import DefaultRouter

from patients import views

router = DefaultRouter()
router.register('patients', views.PatientViewSet)
router.register('medical-records', views.MedicalRecordViewSet)

urlpatterns = router.urls
