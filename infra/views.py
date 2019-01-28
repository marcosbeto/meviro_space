from django.http import HttpResponse
from .models import Secao, Armarios, FuncaoFerramenta, Ferramenta
from rest_framework import viewsets
from .serializers import SecaoSerializer, ArmariosSerializer, FuncaoFerramentaSerializer, FerramentaSerializer

class SecaoViewSet(viewsets.ModelViewSet):
    queryset = Secao.objects.all()
    serializer_class = SecaoSerializer

class ArmariosViewSet(viewsets.ModelViewSet):
    queryset = Armarios.objects.all()
    serializer_class = ArmariosSerializer

class FuncaoFerramentaViewSet(viewsets.ModelViewSet):
    queryset = FuncaoFerramenta.objects.all()
    serializer_class = FuncaoFerramentaSerializer

class FerramentaViewSet(viewsets.ModelViewSet):
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer