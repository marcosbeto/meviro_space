from .models import Recurso, Fornecedor, Bridge
from rest_framework import serializers

class RecursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recurso
        fields = (
					'tipo_recurso',
					'nome',
					'apelido',
					'descricao',
					'fabricante',
					'data_aquisicao',
					'api_financeiro',
					'ultima_atualizacao',
					'voltagem',
					'amperagem',
					'potencia',
					'codigo_meviro',
					'codigo_barra',
					'requer_treinamento',
					'requer_setup',
					'custo_hora',
					'custo_integral',
					'custo_credito',
					'hora_max_dia_usuario',
					'hora_max_sem_usuario',
					'fornecedor'
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



class BridgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bridge
        fields = (
					'recurso',
					'nome',
					'codigo'
				)



