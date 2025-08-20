from rest_framework.routers import DefaultRouter

from clinical_service.views import AppointmentViewSet, ConsultationViewSet, ExaminationViewSet, PrescriptionViewSet

router = DefaultRouter()
router.register('appointment', AppointmentViewSet)
router.register('consultation', ConsultationViewSet)
router.register('examination', ExaminationViewSet)
router.register('Prescription', PrescriptionViewSet)

urlpatterns = router.urls