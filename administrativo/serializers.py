from .models import Pacote, Contrato, PeriodosReservaRecurso, Regra
from rest_framework import serializers

class PacoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pacote
        fields = (
        			'nome',
					'descricao',
					'data_implantacao',
					'ultima_atualizacao',
					'valor_recorrente',
					'valor_unico',
					'valor_periodo_minimo',
					'tipo_periodo_minimo',
					'horas_por_credito',
					'observacoes',
					'pode_agendar_maquinas',
					'regras',
					'assinantes_tem_desconto_recurso',
					'desconto_recurso_percentual',
					'desconto_recurso_valor',
					'cursos',
					'outraAtividade',
					'contrato'
				)

class ContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contrato
        fields = (
        			'nome'
				)

class PeriodosReservaRecursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeriodosReservaRecurso
        fields = (
        			'periodo',
        		)

class RegraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regra
        fields = (
        			'recursos',
					'periodosReservaRecurso'
				)
