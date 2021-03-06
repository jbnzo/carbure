from django.db import models

from core.models import Entity, Lot

class OperatorDeclaration(models.Model):
    operator = models.ForeignKey(Entity, on_delete=models.CASCADE)
    period = models.CharField(max_length=7, blank=False, null=False)
    deadline = models.DateField(blank=False, null=False)

    def __str__(self):
        return '%s - %s' % (self.period, self.operator.name)

    class Meta:
        db_table = 'operator_declaration'
        verbose_name = 'Déclaration de Durabilité'
        verbose_name_plural = 'Déclarations de Durabilité'

class AcceptedLot(models.Model):
    operator = models.ForeignKey(Entity, on_delete=models.CASCADE)
    declaration = models.ForeignKey(OperatorDeclaration, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.operator.name, self.declaration.period)

    class Meta:
        db_table = 'operator_lots'
        verbose_name = 'Lot'
        verbose_name_plural = 'Lots'
