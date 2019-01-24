from django.http import HttpResponse
from .models import Secao, Armarios, IndiceAlerta, Riscos, Fornecedor, NotaFiscal, FuncaoFerramenta, Ferramenta
from rest_framework import viewsets
from .serializers import SecaoSerializer, ArmariosSerializer, IndiceAlertaSerializer, RiscosSerializer, FornecedorSerializer, NotaFiscalSerializer, FuncaoFerramentaSerializer, FerramentaSerializer
from rest_framework.permissions import AllowAny

class SecaoViewSet(viewsets.ModelViewSet):
    queryset = Secao.objects.all()
    serializer_class = SecaoSerializer

class ArmariosViewSet(viewsets.ModelViewSet):
    queryset = Armarios.objects.all()
    serializer_class = ArmariosSerializer

class IndiceAlertaViewSet(viewsets.ModelViewSet):
    queryset = IndiceAlerta.objects.all()
    serializer_class = IndiceAlertaSerializer

class RiscosViewSet(viewsets.ModelViewSet):
    queryset = Riscos.objects.all()
    serializer_class = RiscosSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class NotaFiscalViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer

class FuncaoFerramentaViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = FuncaoFerramenta.objects.all()
    serializer_class = FuncaoFerramentaSerializer

class FerramentaViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer