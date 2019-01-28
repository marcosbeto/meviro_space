from django.http import HttpResponse
from .models import NotaFiscal
from rest_framework import viewsets
from .serializers import NotaFiscalSerializer

class NotaFiscalViewSet(viewsets.ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer
