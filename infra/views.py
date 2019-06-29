from django.http import HttpResponse
from .models import Recurso, Bridge
from rest_framework import viewsets
from .serializers import RecursoSerializer, BridgeSerializer 

class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

class BridgeViewSet(viewsets.ModelViewSet):
    queryset = Bridge.objects.all()
    serializer_class = BridgeSerializer

# class FuncaoFerramentaViewSet(viewsets.ModelViewSet):
#     queryset = FuncaoFerramenta.objects.all()
#     serializer_class = FuncaoFerramentaSerializer

# class FerramentaViewSet(viewsets.ModelViewSet):
#     queryset = Ferramenta.objects.all()
#     serializer_class = FerramentaSerializer