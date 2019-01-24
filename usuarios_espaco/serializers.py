from .models import Permissoes, Assinatura, IntervalosHorarios, DiasSemana, TipoFuncionario, UsuarioEspaco
from rest_framework import serializers


class PermissoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permissoes
        fields = (
        			'nome',
					'descricao'
				)

class AssinaturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assinatura
        fields = (
        			'nome',
					'data_implantacao',
					'ultima_atualizacao',
					'valor',
					'periodo',
					'permissoes',
					'observacoes'
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

class TipoFuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoFuncionario
        fields = (
        			'nome',
					'descricao',
					'permissoes'
				)

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
					'tipo_funcionario',
					'tipo_assinatura',
					'nome_contato_emergencia',
					'telefone_contato_emergencia',
					'tem_plano_saude',
					'nome_plano_saude'
				)

