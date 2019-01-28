from .models import Secao, Armarios, FuncaoFerramenta, Ferramenta
from rest_framework import serializers


class SecaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Secao
        fields = (
        			'nome',
					'descricao',
					'localizacao'
				)

class ArmariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Armarios
        fields = (
        			'nome',
					'apelido',
					'secao'
				)

class FuncaoFerramentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FuncaoFerramenta
        fields = (
					'nome'
				)

class FerramentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ferramenta
        fields = (
					'nome',
					'modelo',
					'funcao_ferramenta',
					'descricao',
					'apelido',
					'fabricante',
					'data_aquisicao',
					'nota_fiscal',
					'fornecedor',
					'foto',
					'voltagem',
					'amperagem',
					'potencia',
					'numero_controle'
				)
