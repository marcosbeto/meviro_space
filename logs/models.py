from django.db import models
from usuarios_meviro.models import UsuarioEspaco
from infra.models import Bridge

class LogAcessoEspacoUsuario(models.Model):
	id_usuario = models.ForeignKey(UsuarioEspaco, blank=True, null=True, on_delete=models.DO_NOTHING)
	data_entrada = models.DateField(blank=True, null=True,)
	hora_entrada = models.TimeField(blank=True, null=True,)
	data_saida = models.DateField(blank=True, null=True,)
	hora_saida = models.TimeField(blank=True, null=True,)

	def __str__(self):
		return u'%s [%s]' % (self.id_usuario, self.data_entrada)
	
	class Meta:
		verbose_name = "Registro de Log de Acesso"
		verbose_name_plural = "Logs de Acesso"

class LogUsoFerramentaUsuario(models.Model):
	id_bridge = models.ForeignKey(Bridge, blank=True, null=True, on_delete=models.DO_NOTHING)
	id_usuario = models.ForeignKey(UsuarioEspaco, blank=True, null=True, on_delete=models.DO_NOTHING)
	data_ativacao = models.DateField(blank=True, null=True,)
	hora_ativacao = models.TimeField(blank=True, null=True,)
	data_desativacao = models.DateField(blank=True, null=True,)
	hora_desativacao = models.TimeField(blank=True, null=True,)
	tempo_uso = models.TimeField(blank=True, null=True,)

	def __str__(self):
		return u'%s usou %s por %s' % (self.id_usuario.primeiro_nome, self.id_bridge.nome, self.tempo_uso)
	
	class Meta:
		verbose_name = "Registro de Log de Uso"
		verbose_name_plural = "Logs de Uso"
