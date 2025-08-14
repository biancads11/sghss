from django.db import models
from core.models import BaseModel

class Patient(BaseModel):
    """
    Corresponds to 'pacientes'
    Stores personal and contact information for patients.
    """
    name = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField(db_column='data_nascimento', null=True, blank=True)
    gender = models.CharField(db_column='sexo', max_length=1, null=True, blank=True)
    phone = models.CharField(db_column='telefone', max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.TextField(db_column='endereco', null=True, blank=True)
    emergency_details = models.TextField(db_column='dados_emergencia', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pacientes'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

class MedicalRecord(BaseModel):
    """
    Corresponds to 'prontuarios'
    Central medical record for a patient.
    """
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, db_column='paciente_id')
    responsible_physician = models.ForeignKey('professionals.HealthProfessional', on_delete=models.SET_NULL, null=True, db_column='medico_responsavel_id')
    general_observations = models.TextField(db_column='observacoes_gerais', null=True, blank=True)
    # Note: 'data_abertura' is covered by 'created_at' from BaseModel.

    class Meta:
        db_table = 'prontuarios'
        verbose_name = 'Medical Record'
        verbose_name_plural = 'Medical Records'