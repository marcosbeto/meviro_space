# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from meviro_space import constants

# from localflavor.br.forms import BRCPFField, BRStateChoiceField, BRStateSelect, BRZipCodeField

class Permissoes(models.Model):
	nome = models.CharField(max_length=30)
	descricao = models.CharField(max_length=200)

	def __str__(self):
		return u'%s' % (self.nome)

	class Meta:
		verbose_name_plural = "Tipos de Permissões"


class Assinatura(models.Model):
    nome = models.CharField(max_length=30)
    data_implantacao = models.DateField()
    ultima_atualizacao =  models.DateField(blank=True)
    valor = models.IntegerField(blank=True)
    periodo = models.CharField(max_length=30)
    permissoes = models.ForeignKey(Permissoes, models.SET_NULL,blank=True,null=True)
    observacao = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
    	return u'%s - %s' % (self.nome, self.periodo)

    class Meta:
    	verbose_name_plural = "Tipos de Assinatura"


# class Avatar(models.Model):
#     nome = models.CharField(max_length=30)
#     descricao = models.CharField(max_length=200)
#     imagem_avatar = models.ImageField(upload_to='uploads/fotos_usuarios_espaco')
	
# 	class Meta:
# 		verbose_name_plural = "Tipos de Avatar"

class IntervalosHorarios(models.Model):
	intervalo = models.CharField(max_length=15)

	def __str__(self):
		return u'%s' % (self.intervalo)


	class Meta:
		verbose_name_plural = "[fixo] Intervalos de Horários"

class DiasSemana(models.Model):
	numero_dia = models.IntegerField(default=0)
	dia = models.CharField(max_length=15)

	def __str__(self):
		return u'%s' % (self.dia)

	class Meta:
		verbose_name_plural = "[fixo] Dias da Semana"

class TipoFuncionario(models.Model):
	nome = models.CharField(max_length=30)
	descricao = models.CharField(max_length=200)
	permissoes = models.ForeignKey(Permissoes, models.SET_NULL,blank=True,null=True)

	def __str__(self):
		return u'%s' % (self.nome)

	class Meta:
		verbose_name_plural = "Tipos de Funcionários"

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
	# avatar = models.ForeignKey(Avatar, models.SET_NULL, blank=True, null=True) #when the reference is deleted the item will not be deleted
	apelido = models.CharField(max_length=30, blank=True)
	dias_provaveis = models.ForeignKey(DiasSemana, models.SET_NULL,blank=True,null=True) #when the reference is deleted the item will not be deleted
	horarios_provaveis = models.ForeignKey(IntervalosHorarios, models.SET_NULL,blank=True,null=True)
	tipo_funcionario = models.ForeignKey(TipoFuncionario, models.SET_NULL,blank=True,null=True)
	tipo_assinatura = models.ForeignKey(Assinatura, models.SET_NULL,blank=True,null=True)
	nome_contato_emergencia = models.CharField(max_length=50, blank=True)
	telefone_contato_emergencia = models.CharField(max_length=30, blank=True)
	tem_plano_saude = models.BooleanField(default=False)
	nome_plano_saude = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return u'%s %s' % (self.primeiro_nome, self.sobrenome)

	class Meta:
		verbose_name_plural = "Usuários do Espaço"