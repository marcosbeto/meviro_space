# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from meviro_space import constants

class Fornecedor(models.Model):
	nome = models.CharField(max_length=50, verbose_name="Nome do Fornecedor")
	cnpj = models.CharField(max_length=30, blank=True, null=True, verbose_name="CNPJ do Fornecedor")
	endereco = models.CharField(max_length=200, blank=True, null=True, verbose_name="Nome do Fornecedor")
	site = models.CharField(max_length=70, blank=True, null=True)
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=2, choices=constants.STATE_CHOICES)
	telefone = models.CharField(max_length=30, blank=True, null=True)
	nome_contato = models.CharField(max_length=30, blank=True, null=True)
	email_contato = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return u'%s' % (self.nome)

	class Meta:
		verbose_name = "Fornecedor"
		verbose_name_plural = "Fornecedores"


class Recurso(models.Model):

	TIPOS_RECURSOS = [
	    ('porta', 'Porta'),
		('terminal check-in/out', 'Terminal Check-in/out'),
		('sala', 'Sala'),
		('bancada', 'Bancada'),
		('maquina', 'Maquina'),
		('ferramenta manual', 'Ferramenta Manual'),
		('ferramenta eletrica', 'Ferramenta Elétrica'),
		('ferramenta pneumatica', 'Ferramenta Pneumática'),
		('material insumo', 'Material Insumo')
	]

	tipo_recurso = models.CharField(max_length=30, choices=TIPOS_RECURSOS)
	nome = models.CharField(max_length=30, verbose_name="Nome do Recurso", help_text="Aqui vai um texto de ajuda mesmo.")
	apelido = models.CharField(max_length=30, blank=True, null=True, verbose_name="O recurso tem algum apelido?")
	descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
	fabricante = models.CharField(max_length=30, blank=True, null=True)
	data_aquisicao = models.DateField(blank=True, null=True, verbose_name="Data da aquisição")
	ultima_atualizacao =  models.DateField(blank=True, null=True, verbose_name="Última atualização")
	voltagem = models.CharField(max_length=10, blank=True, null=True, choices=[('110v','110'),('220v','220')])
	amperagem = models.IntegerField(blank=True, null=True)
	potencia = models.IntegerField(blank=True, null=True, verbose_name="Potência")
	codigo_meviro = models.IntegerField(blank=True, null=True, verbose_name="Código Referência MeViro")
	requer_treinamento = models.BooleanField(default=False, verbose_name="Requer treinamento para o uso?")
	requer_setup = models.BooleanField(default=False, verbose_name="Requer algum setup inicial para o uso?")
	custo_hora = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Custo de Uso por Hora")
	custo_integral = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Custo de Uso Integral")
	custo_credito = models.IntegerField(blank=True, null=True, verbose_name="Custo de Uso por Crédito")
	hora_max_dia_usuario = models.IntegerField(blank=True, null=True, verbose_name="Número máximo de horas de utilização por dia por usuário")
	hora_max_sem_usuario = models.IntegerField(blank=True, null=True, verbose_name="Número máximo de horas de utilização por semana por usuário")
	fornecedor = models.ForeignKey(Fornecedor, models.SET_NULL, blank=True, null=True)
	api_financeiro = models.CharField(max_length=30)
	observacoes = models.TextField(null=True, blank=True, verbose_name="Observações")

	def __str__(self):
		return u'%s' % (self.nome)

	class Meta:
		verbose_name = "Recurso"
		verbose_name_plural = "Recursos"
	

class Bridge(models.Model):
	recurso = models.ForeignKey(Recurso, on_delete=models.DO_NOTHING, verbose_name="Com qual recurso se conecta?")
	nome =  models.CharField(max_length=30, blank=True, verbose_name="Nome da Bridge")
	codigo =  models.CharField(max_length=30, blank=True, verbose_name="Código da Bridge")

	def __str__(self):
		return u'%s (id:%s)' % (self.nome, self.id)
	
	class Meta:
		verbose_name = "Brigde"
		verbose_name_plural = "Brigdes"


# class Arduino(models.Model):
# 	nome =  models.CharField(max_length=30, blank=True)
# 	codigo =  models.CharField(max_length=30, blank=True)

# 	def __str__(self):
# 		return u'%s (id:%s)' % (self.nome, self.id)
	
# 	class Meta:
# 		verbose_name = "Brigde"
# 		verbose_name_plural = "Brigdes"


# class BridgeAuth(models.Model):
# 	id_bridge = models.ForeignKey(Bridge, blank=True, null=True, on_delete=models.DO_NOTHING)
# 	id_recurso = models.ForeignKey(Recurso, blank=True, null=True, on_delete=models.DO_NOTHING)
	
# 	def __str__(self):
# 		return u'%s(id:%s) <> %s(id:%s)' % (self.id_bridge.nome, self.id_bridge.id, self.id_recurso.nome, self.id_recurso.id)
	
# 	class Meta:
# 		verbose_name = "Brigde <> Recurso"
# 		verbose_name_plural = "Brigdes <> Recursos"




