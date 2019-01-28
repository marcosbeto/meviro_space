from .models import NotaFiscal
from rest_framework import serializers

class NotaFiscalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = (
        			'identificacao',
					'fornecedor',
					'nome',
				)