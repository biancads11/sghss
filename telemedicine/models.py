from django.db import models
from core.models import BaseModel

class Teleconsultation(BaseModel):
    """
    Corresponds to 'teleconsultas'
    Manages remote video consultations.
    """
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, db_column='paciente_id')
    professional = models.ForeignKey('professionals.HealthProfessional', on_delete=models.SET_NULL, null=True, db_column='profissional_id')
    timestamp = models.DateTimeField(db_column='data_hora')
    video_call_link = models.URLField(db_column='link_videochamada', max_length=500)
    status = models.CharField(max_length=30)
    recording_url = models.URLField(db_column='gravacao_url', max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'teleconsultas'
        verbose_name = 'Teleconsultation'
        verbose_name_plural = 'Teleconsultations'

class TeleconsultationRecord(BaseModel):
    """
    Corresponds to 'registros_teleconsulta'
    Links a teleconsultation to other records like prescriptions and medical records.
    """
    teleconsultation = models.ForeignKey('telemedicine.Teleconsultation', on_delete=models.CASCADE, db_column='teleconsulta_id')
    medical_record = models.ForeignKey('patients.MedicalRecord', on_delete=models.CASCADE, db_column='prontuario_id')
    prescription = models.ForeignKey('clinical_service.Prescription', on_delete=models.SET_NULL, null=True, blank=True, db_column='prescricao_id')
    observations = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'registros_teleconsulta'
        verbose_name = 'Teleconsultation Record'
        verbose_name_plural = 'Teleconsultation Records'