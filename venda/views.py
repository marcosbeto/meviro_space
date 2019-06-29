from django.shortcuts import render
from .serializers import OrdemDeServicoSerializer, VendaPacotesPorUsuarioSerializer, VendaCreditosSerializer
from .models import OrdemDeServico, VendaPacotesPorUsuario, VendaCreditos

class OrdemDeServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemDeServico.objects.all()
    serializer_class = OrdemDeServicoSerializer

class VendaPacotesPorUsuarioViewSet(viewsets.ModelViewSet):
    queryset = VendaPacotesPorUsuario.objects.all()
    serializer_class = VendaPacotesPorUsuarioSerializer

class VendaCreditosViewSet(viewsets.ModelViewSet):
    queryset = VendaCreditosSerializer.objects.all()
    serializer_class = VendaCreditosSerializer