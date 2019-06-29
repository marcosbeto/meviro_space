from .models import TreinamentoEmEquipamentos, Cursos, OutrasAtividades
from rest_framework import serializers

class TreinamentoEmEquipamentosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recursos
        fields = (
					'recursos',
				)

class CursosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fornecedor
        fields = (
					'precisa_treinamento',
					'treinamentoEmEquipamentos',
					'nome',
					'dates'
				)

class OutrasAtividadesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bridges
        fields = (
					'treinamentoEmEquipamentos',
					'nome',
					'dates'
				)



