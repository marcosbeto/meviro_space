from .models import OrdemDeServico, VendaPacotesPorUsuario, VendaCreditos
from rest_framework import serializers

class OrdemDeServicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrdemDeServico
        fields = (
        			'usuario_meviro',
					'status_os',
					'numero_os',
					'data_inicio',
					'previsao_entrega',
					'descricao_servico',
					'observacoes'
				)

class VendaPacotesPorUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendaPacotesPorUsuario
        fields = (
        			'usuario_meviro',
					'pacotes',
					'data_assinatura',
					'contratos',
					'status'
				)

class VendaCreditosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendaCreditos
        fields = (
        			'usuario_meviro',
					'data_venda',
					'contratos',
					'numero_creditos'
				)