from django.db import models
from core.models import BaseModel

class Audit(BaseModel):
    """
    Corresponds to 'auditorias'
    Logs changes to data for auditing purposes.
    """
    user = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True, db_column='usuario_id')
    action = models.TextField()
    affected_table = models.CharField(db_column='tabela_afetada', max_length=100)
    record_id = models.IntegerField(db_column='id_registro')
    data_before = models.JSONField(db_column='dados_antes', null=True, blank=True)
    data_after = models.JSONField(db_column='dados_depois', null=True, blank=True)
    # Note: 'data_hora' is covered by 'created_at' from BaseModel.

    class Meta:
        db_table = 'auditorias'
        verbose_name = 'Audit'
        verbose_name_plural = 'Audits'

class Backup(BaseModel):
    """
    Corresponds to 'backups'
    Records information about database backups.
    """
    backup_type = models.CharField(db_column='tipo', max_length=50)
    storage_location = models.TextField(db_column='local_armazenamento')
    status = models.CharField(max_length=30)
    # Note: 'data_backup' is covered by 'created_at' from BaseModel.

    class Meta:
        db_table = 'backups'
        verbose_name = 'Backup'
        verbose_name_plural = 'Backups'

class FinancialReport(BaseModel):
    """
    Corresponds to 'relatorios_financeiros'
    Stores generated financial reports.
    """
    start_date = models.DateField(db_column='data_inicio')
    end_date = models.DateField(db_column='data_fim')
    total_revenue = models.DecimalField(db_column='receita_total', max_digits=12, decimal_places=2, null=True, blank=True)
    total_expense = models.DecimalField(db_column='despesa_total', max_digits=12, decimal_places=2, null=True, blank=True)
    balance = models.DecimalField(db_column='saldo', max_digits=12, decimal_places=2, null=True, blank=True)
    report_type = models.CharField(db_column='tipo', max_length=50)

    class Meta:
        db_table = 'relatorios_financeiros'
        verbose_name = 'Financial Report'
        verbose_name_plural = 'Financial Reports'

class SystemStatus(BaseModel):
    """
    Corresponds to 'status_sistema'
    Monitors the health and performance of system modules.
    """
    module_name = models.CharField(db_column='nome_modulo', max_length=100)
    operational_status = models.CharField(db_column='status_operacional', max_length=30)
    response_time_ms = models.IntegerField(null=True, blank=True)
    last_check = models.DateTimeField(db_column='ultima_verificacao')

    class Meta:
        db_table = 'status_sistema'
        verbose_name = 'System Status'
        verbose_name_plural = 'System Statuses'