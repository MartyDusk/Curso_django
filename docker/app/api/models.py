from django.db import models


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class OrdenExterna(models.Model):
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        related_name='ordenes'
    )
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'Orden {self.id}'


class DetalleOrdenExterna(models.Model):
    orden = models.ForeignKey(
        OrdenExterna,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    producto_id = models.IntegerField()
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'Detalle {self.id}'
