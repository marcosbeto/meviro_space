# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from meviro_space import constants
from administrativo.models import Assinatura, DiasSemana, IntervalosHorarios

class UsuarioEspaco(models.Model):
	primeiro_nome = models.CharField(max_length=30)
	sobrenome = models.CharField(max_length=200)
	data_nascimento = models.DateField()
	email = models.EmailField(max_length=50)
	endereco = models.CharField(max_length=200)
	cidade = models.CharField(max_length=30)
	estado = models.CharField(max_length=2, choices=constants.STATE_CHOICES,  blank=True)
	telefone_celular = models.CharField(max_length=30)
	telefone_residencial = models.CharField(max_length=30, blank=True)
	telefone_comercial = models.CharField(max_length=30, blank=True)
	cpf = models.CharField(max_length=30)
	rg = models.CharField(max_length=30)
	foto = models.ImageField(upload_to='fotos_usuarios_espaco', blank=True)
	apelido = models.CharField(max_length=30, blank=True)
	tipo_assinatura = models.ForeignKey(Assinatura, models.SET_NULL,blank=True,null=True)
	nome_contato_emergencia = models.CharField(max_length=50, blank=True)
	telefone_contato_emergencia = models.CharField(max_length=30, blank=True)
	tem_plano_saude = models.BooleanField(default=False)
	nome_plano_saude = models.CharField(max_length=50, blank=True)

	def restart_button(self):
		return mark_safe("<a href='record_rfid/" + str(self.id) + "/' style='background-color: #ffcd00;padding: 4px 8px;color: #333333;border-radius: 2px;font-weight: bold;font-size: 10pt;'>Enviar comando</a>")
    
	restart_button.allow_tags = True
	restart_button.short_description = "Gravar Cartão"

	def __str__(self):
		return u'%s %s' % (self.primeiro_nome, self.sobrenome)

	class Meta:
		verbose_name_plural = "Usuários do Espaço"
		verbose_name = "Usuário do Espaço"
		 
		
                


class UsuarioDiasSemana(models.Model):
	id_usuario = models.ForeignKey(UsuarioEspaco, on_delete=models.DO_NOTHING)
	id_dias_provaveis = models.ForeignKey(DiasSemana, on_delete=models.DO_NOTHING)

	def __str__(self):
		return u'%s %s' % (self.id_usuario.primeiro_nome, self.id_dias_provaveis.dia)

	class Meta:
		verbose_name_plural = "Prováveis Dias de Uso"
		verbose_name = "Provável Dia de Uso"

class UsuarioIntervalosHorarios(models.Model):
	id_usuario = models.ForeignKey(UsuarioEspaco, on_delete=models.DO_NOTHING)
	id_intervalos_horarios = models.ForeignKey(IntervalosHorarios, on_delete=models.DO_NOTHING)

	def __str__(self):
		return u'%s %s' % (self.id_usuario.primeiro_nome, self.id_intervalos_horarios.id_intervalos_horarios)

	class Meta:
		verbose_name_plural = "Prováveis Horários de Uso"
		verbose_name = "Provável Horário de Uso"