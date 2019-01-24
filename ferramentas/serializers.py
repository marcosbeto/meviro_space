from .models import Secao, Armarios, IndiceAlerta, Riscos, Fornecedor, NotaFiscal, FuncaoFerramenta, Ferramenta
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

class IndiceAlertaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndiceAlerta
        fields = (
        			'indice_alerta',
        			'descricao'
				)

class RiscosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Riscos
        fields = (
        			'nome',
        			'descricao',
        			'alerta'
				)

class FornecedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fornecedor
        fields = (
        			'nome',
					'endereco',
					'site',
					'cidade',
					'estado',
					'telefone',
					'nome_contato',
					'email_contato'
				)

class NotaFiscalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = (
        			'identificacao',
					'fornecedor',
					'nome',
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
