from rest_framework.routers import DefaultRouter

from clinical_service import views

router = DefaultRouter()
router.register('appointment', views.AppointmentViewSet)
router.register('consultation', views.ConsultationViewSet)
router.register('examination', views.ExaminationViewSet)
router.register('Prescription', views.PrescriptionViewSet)

urlpatterns = router.urls
