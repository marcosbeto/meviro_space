from django.http import HttpResponse
from .models import Pacote, Contrato, PeriodosReservaRecurso, Regra
from rest_framework import viewsets
from .serializers import PacoteSerializer, ContratoSerializer, PeriodosReservaRecursoSerializer, RegraSerializer

class PacoteViewSet(viewsets.ModelViewSet):
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class PeriodosReservaRecursoViewSet(viewsets.ModelViewSet):
    queryset = PeriodosReservaRecurso.objects.all()
    serializer_class = PeriodosReservaRecursoSerializer

class RegraViewSet(viewsets.ModelViewSet):
    queryset = Regra.objects.all()
    serializer_class = RegraSerializer


