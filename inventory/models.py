from django.db import models
from core.models import BaseModel

class Supply(BaseModel):
    """
    Corresponds to 'suprimentos'
    Represents a type of medical supply or material.
    """
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100, null=True, blank=True)
    stock_quantity = models.IntegerField(db_column='quantidade_estoque', default=0)
    unit_of_measure = models.CharField(db_column='unidade_medida', max_length=20, null=True, blank=True)
    # Assuming 'fornecedor_id' might reference an external system or just be informational.
    # If you had a 'Suppliers' model, this would be a ForeignKey.
    supplier_id = models.IntegerField(db_column='fornecedor_id', null=True, blank=True)

    class Meta:
        db_table = 'suprimentos'
        verbose_name = 'Supply'
        verbose_name_plural = 'Supplies'

class StockMovement(BaseModel):
    """
    Corresponds to 'movimentacoes_estoque'
    Logs the entry or exit of supplies from inventory.
    """
    supply = models.ForeignKey('inventory.Supply', on_delete=models.CASCADE, db_column='suprimento_id')
    professional = models.ForeignKey('professionals.HealthProfessional', on_delete=models.SET_NULL, null=True, db_column='profissional_id')
    movement_type = models.CharField(db_column='tipo', max_length=20) # e.g., 'Entry', 'Exit'
    quantity = models.IntegerField()
    # Note: 'data' is covered by 'created_at' from BaseModel.

    class Meta:
        db_table = 'movimentacoes_estoque'
        verbose_name = 'Stock Movement'
        verbose_name_plural = 'Stock Movements'