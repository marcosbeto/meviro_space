from django.http import HttpResponse
from .models import Permissoes, Assinatura, IntervalosHorarios, DiasSemana, TipoFuncionario, UsuarioEspaco
from rest_framework import viewsets
from .serializers import PermissoesSerializer, AssinaturaSerializer, IntervalosHorariosSerializer, DiasSemanaSerializer, TipoFuncionarioSerializer, UsuarioEspacoSerializer
from rest_framework.permissions import AllowAny

class PermissoesViewSet(viewsets.ModelViewSet):
    queryset = Permissoes.objects.all()
    serializer_class = PermissoesSerializer

class AssinaturaViewSet(viewsets.ModelViewSet):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer

class IntervalosHorariosViewSet(viewsets.ModelViewSet):
    queryset = IntervalosHorarios.objects.all()
    serializer_class = IntervalosHorariosSerializer

class DiasSemanaViewSet(viewsets.ModelViewSet):
    queryset = DiasSemana.objects.all()
    serializer_class = DiasSemanaSerializer

class TipoFuncionarioViewSet(viewsets.ModelViewSet):
    queryset = TipoFuncionario.objects.all()
    serializer_class = TipoFuncionarioSerializer

class UsuarioEspacoViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = UsuarioEspaco.objects.all()
    serializer_class = UsuarioEspacoSerializer


