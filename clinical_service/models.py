from django.db import models
from core.models import BaseModel

class Appointment(BaseModel):
    """
    Corresponds to 'atendimentos'
    A general record for any patient-professional interaction.
    """
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, db_column='paciente_id')
    professional = models.ForeignKey('professionals.HealthProfessional', on_delete=models.SET_NULL, null=True, db_column='profissional_id')
    appointment_type = models.CharField(db_column='tipo', max_length=50)
    timestamp = models.DateTimeField(db_column='data_hora')
    reason = models.TextField(db_column='motivo', null=True, blank=True)
    observations = models.TextField(db_column='observacoes', null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'atendimentos'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

class Consultation(BaseModel):
    """
    Corresponds to 'consultas'
    Details for a specific medical consultation.
    """
    appointment = models.ForeignKey('clinical_service.Appointment', on_delete=models.CASCADE, db_column='atendimento_id')
    specialty = models.CharField(db_column='especialidade', max_length=100)
    location = models.CharField(db_column='local', max_length=100, null=True, blank=True)
    consultation_type = models.CharField(db_column='tipo_consulta', max_length=20, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'consultas'
        verbose_name = 'Consultation'
        verbose_name_plural = 'Consultations'

class Examination(BaseModel):
    """
    Corresponds to 'exames'
    Records for medical exams/tests.
    """
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, db_column='paciente_id')
    requesting_professional = models.ForeignKey('professionals.HealthProfessional', on_delete=models.SET_NULL, null=True, db_column='profissional_solicitante_id')
    exam_type = models.CharField(db_column='tipo_exame', max_length=100)
    request_date = models.DateField(db_column='data_solicitacao')
    completion_date = models.DateField(db_column='data_realizacao', null=True, blank=True)
    result = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'exames'
        verbose_name = 'Examination'
        verbose_name_plural = 'Examinations'

class Prescription(BaseModel):
    """
    Corresponds to 'prescricoes'
    Medical prescriptions issued during an appointment.
    """
    appointment = models.ForeignKey('clinical_service.Appointment', on_delete=models.CASCADE, db_column='atendimento_id')
    professional = models.ForeignKey('professionals.HealthProfessional', on_delete=models.SET_NULL, null=True, db_column='profissional_id')
    prescription_text = models.TextField(db_column='texto_prescricao')
    digital_signature = models.TextField(db_column='assinatura_digital', null=True, blank=True)
    # Note: 'data' is covered by 'created_at' from BaseModel.

    class Meta:
        db_table = 'prescricoes'
        verbose_name = 'Prescription'
        verbose_name_plural = 'Prescriptions'

class DigitalReceipt(BaseModel):
    """
    Corresponds to 'receitas_digitais'
    The digital file (e.g., PDF) of a prescription.
    """
    prescription = models.ForeignKey('clinical_service.Prescription', on_delete=models.CASCADE, db_column='prescricao_id')
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, db_column='paciente_id')
    expiration_date = models.DateField(db_column='data_validade', null=True, blank=True)
    pdf_file = models.TextField(db_column='arquivo_pdf', help_text="Path or link to the PDF file.")

    class Meta:
        db_table = 'receitas_digitais'
        verbose_name = 'Digital Receipt'
        verbose_name_plural = 'Digital Receipts'