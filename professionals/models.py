from django.db import models
from simple_history.models import HistoricalRecords

from core.models import BaseModel


class HealthProfessional(BaseModel):
    """
    Corresponds to 'profissionais_saude'
    Stores information about doctors, nurses, and other health staff.
    """
    name = models.CharField(max_length=150)
    professional_registry = models.CharField(db_column='registro_profissional', max_length=50, null=True, blank=True)
    specialty = models.CharField(db_column='especialidade', max_length=100, null=True, blank=True)
    position = models.CharField(db_column='cargo', max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(db_column='telefone', max_length=20, null=True, blank=True)
    hospital_unit = models.ForeignKey('infrastructure.HospitalUnit', on_delete=models.SET_NULL, null=True,
                                      db_column='unidade_id')
    history = HistoricalRecords(table_name='"history"."profissionais_saude"')

    def __str__(self):
        return f"{self.name} ({self.specialty})"

    class Meta:
        db_table = 'profissionais_saude'
        verbose_name = 'Health Professional'
        verbose_name_plural = 'Health Professionals'


class Schedule(BaseModel):
    """
    Corresponds to 'agendas'
    Manages the schedule and availability of health professionals.
    """
    professional = models.ForeignKey('professionals.HealthProfessional', on_delete=models.CASCADE,
                                     db_column='profissional_id')
    date = models.DateField(db_column='data')
    start_time = models.TimeField(db_column='hora_inicio')
    end_time = models.TimeField(db_column='hora_fim')
    event_type = models.CharField(db_column='tipo_evento', max_length=100, null=True, blank=True)
    is_available = models.BooleanField(db_column='disponibilidade', default=True)

    class Meta:
        db_table = 'agendas'
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
