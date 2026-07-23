from rest_framework import serializers
from .models import Sucursal, OrdenExterna, DetalleOrdenExterna


class DetalleOrdenExternaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrdenExterna
        fields = ['id', 'nombre']


class OrdenExternaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenExterna
        fields = ['id', 'sucursal', 'total', 'detalles']


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['id', 'nombre', 'ordenes']
