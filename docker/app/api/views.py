from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

# Create your views here.


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    permission_classes = [IsAuthenticated]


class OrdenExternaViewSet(viewsets.ModelViewSet):
    queryset = OrdenExterna.objects.all()
    serializer_class = OrdenExternaSerializer
    permission_classes = [IsAuthenticated]


class DetalleOrdenExternaViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrdenExterna.objects.all()
    serializer_class = DetalleOrdenExternaSerializer
    permission_classes = [IsAuthenticated]
