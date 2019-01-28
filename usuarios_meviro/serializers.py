from .models import UsuarioEspaco
from rest_framework import serializers

class UsuarioEspacoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsuarioEspaco
        fields = (
        			'primeiro_nome',
					'sobrenome',
					'data_nascimento',
					'email',
					'endereco',
					'cidade',
					'estado',
					'telefone_celular',
					'telefone_residencial',
					'telefone_comercial',
					'cpf',
					'rg',
					'foto',
					'apelido',
					'dias_provaveis',
					'horarios_provaveis',
					# 'tipo_funcionario',
					'tipo_assinatura',
					'nome_contato_emergencia',
					'telefone_contato_emergencia',
					'tem_plano_saude',
					'nome_plano_saude'
				)

