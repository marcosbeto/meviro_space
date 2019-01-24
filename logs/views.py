from django.http import HttpResponse
from .models import LogAcessoEspacoUsuario, LogUsoFerramentaUsuario
from rest_framework import viewsets
from .serializers import LogAcessoEspacoUsuarioSerializer, LogUsoFerramentaUsuarioSerializer
from rest_framework.permissions import AllowAny

class LogAcessoEspacoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = LogAcessoEspacoUsuario.objects.all()
    serializer_class = LogAcessoEspacoUsuarioSerializer

class LogUsoFerramentaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = LogUsoFerramentaUsuario.objects.all()
    serializer_class = LogUsoFerramentaUsuarioSerializer