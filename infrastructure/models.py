from django.db import models
from core.models import BaseModel

class HospitalUnit(BaseModel):
    """
    Corresponds to 'unidades_hospitalares'
    Represents a hospital, clinic, or other healthcare facility.
    """
    name = models.CharField(max_length=150)
    address = models.TextField(db_column='endereco', null=True, blank=True)
    unit_type = models.CharField(db_column='tipo_unidade', max_length=50)
    contact_info = models.CharField(db_column='contato', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'unidades_hospitalares'
        verbose_name = 'Hospital Unit'
        verbose_name_plural = 'Hospital Units'

class Bed(BaseModel):
    """
    Corresponds to 'leitos'
    Represents a single bed within a hospital unit.
    """
    hospital_unit = models.ForeignKey('infrastructure.HospitalUnit', on_delete=models.CASCADE, db_column='unidade_id')
    number = models.CharField(max_length=10)
    bed_type = models.CharField(db_column='tipo', max_length=50)
    status = models.CharField(max_length=20) # e.g., 'Available', 'Occupied', 'Maintenance'
    occupying_patient = models.ForeignKey('patients.Patient', on_delete=models.SET_NULL, null=True, blank=True, db_column='paciente_ocupante_id')
    occupation_date = models.DateField(db_column='data_ocupacao', null=True, blank=True)

    class Meta:
        db_table = 'leitos'
        verbose_name = 'Bed'
        verbose_name_plural = 'Beds'

class Hospitalization(BaseModel):
    """
    Corresponds to 'internacoes'
    Records a patient's admission and stay in a hospital bed.
    """
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, db_column='paciente_id')
    bed = models.ForeignKey('infrastructure.Bed', on_delete=models.SET_NULL, null=True, db_column='leito_id')
    entry_date = models.DateField(db_column='data_entrada')
    discharge_date = models.DateField(db_column='data_alta', null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'internacoes'
        verbose_name = 'Hospitalization'
        verbose_name_plural = 'Hospitalizations'