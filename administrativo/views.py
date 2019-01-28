from django.http import HttpResponse
from .models import Assinatura, IntervalosHorarios, DiasSemana, Fornecedor
from rest_framework import viewsets
from .serializers import AssinaturaSerializer, IntervalosHorariosSerializer, DiasSemanaSerializer, FornecedorSerializer

class AssinaturaViewSet(viewsets.ModelViewSet):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer

class IntervalosHorariosViewSet(viewsets.ModelViewSet):
    queryset = IntervalosHorarios.objects.all()
    serializer_class = IntervalosHorariosSerializer

class DiasSemanaViewSet(viewsets.ModelViewSet):
    queryset = DiasSemana.objects.all()
    serializer_class = DiasSemanaSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


