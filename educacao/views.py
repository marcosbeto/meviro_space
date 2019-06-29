from django.http import HttpResponse
from .models import TreinamentoEmEquipamentos, Cursos, OutrasAtividadesSerializer
from rest_framework import viewsets
from .serializers import TreinamentoEmEquipamentosSerializer, CursosSerializer, OutrasAtividadesSerializer

class TreinamentoEmEquipamentosViewSet(viewsets.ModelViewSet):
    queryset = TreinamentoEmEquipamentos.objects.all()
    serializer_class = TreinamentoEmEquipamentosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class OutrasAtividadesSerializerViewSet(viewsets.ModelViewSet):
    queryset = OutrasAtividadesSerializer.objects.all()
    serializer_class = OutrasAtividadesSerializerSerializer
