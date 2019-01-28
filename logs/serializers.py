from .models import LogAcessoEspacoUsuario, LogUsoFerramentaUsuario
from rest_framework import serializers

class LogAcessoEspacoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAcessoEspacoUsuario
        fields = (
        			'id_usuario',
					'data_entrada',
					'hora_entrada',
					'data_saida',
					'hora_saida'
				)

class LogUsoFerramentaUsuarioSerializer(serializers.ModelSerializer):
    
    # included_serializers = {'log-uso-list': UsuarioEspacoSerializer}

    class Meta:
        model = LogUsoFerramentaUsuario
        fields = (
        			'id_ferramenta',
					'id_usuario',
					'data_ativacao',
					'hora_ativacao',
					'data_desativacao',
					'hora_desativacao',
					'tempo_uso'
				)