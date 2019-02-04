from .models import Assinatura, IntervalosHorarios, DiasSemana, Fornecedor
from rest_framework import serializers

class AssinaturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assinatura
        fields = (
        			'nome',
					'data_implantacao',
					'ultima_atualizacao',
					'valor',
					'periodo',
					'observacao'
				)

class IntervalosHorariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntervalosHorarios
        fields = (
        			'intervalo'
				)

class DiasSemanaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiasSemana
        fields = (
        			'numero_dia',
        			'dia'
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
