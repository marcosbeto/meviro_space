from .models import UsuarioEspaco, Agendamento
from rest_framework import serializers

class UsuarioEspacoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsuarioEspaco
        fields = (
        			'contratos',
					'pacotes',
					'treinamentoEmEquipamentos',
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
					'nome_contato_emergencia',
					'telefone_contato_emergencia',
					'tem_plano_saude',
					'nome_plano_saude'
				)

class AgendamentoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Agendamento
		fields = (
					'usuarios', 
					'recursos', 
					'data', 
					'horario' 
				)