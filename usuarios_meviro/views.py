from django.http import HttpResponse
from .models import UsuarioEspaco
from rest_framework import viewsets
from .serializers import UsuarioEspacoSerializer

class UsuarioEspacoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioEspaco.objects.all()
    serializer_class = UsuarioEspacoSerializer


