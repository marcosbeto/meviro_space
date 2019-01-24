# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from meviro_space import constants

# from localflavor.br.forms import BRCPFField, BRStateChoiceField, BRStateSelect, BRZipCodeField

class Secao(models.Model):
	nome = models.CharField(max_length=50)
	descricao = models.CharField(max_length=200)
	localizacao = models.CharField(max_length=50)

	def __str__(self):
		return u'%s' % (self.nome)
	
	class Meta:
		verbose_name = "Seção"
		verbose_name_plural = "Seções"


class Armarios(models.Model):
	nome = models.CharField(max_length=50)
	apelido = models.CharField(max_length=50)
	secao = models.ForeignKey(Secao, models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return u'%s - %s' % (self.nome, self.secao)
	
	class Meta:
		verbose_name = "Armário"
		verbose_name_plural = "Armários"


class IndiceAlerta(models.Model):
	indice_alerta = models.IntegerField()
	descricao = models.CharField(max_length=200)

	def __str__(self):
		return u'%i' % (self.indice_alerta)
	
	class Meta:
		verbose_name = "Índice de Alerta"
		verbose_name_plural = "[fixo] Índices de Alertas"


class Riscos(models.Model):
	nome = models.CharField(max_length=50)
	descricao = models.CharField(max_length=200)
	alerta = models.ForeignKey(IndiceAlerta, models.SET_NULL, blank=True, null=True)
	
	def __str__(self):
		return u'%s - Alerta: ' % (self.nome, self.alerta)

	class Meta:
		verbose_name = "Risco"
		verbose_name_plural = "Riscos"


class Fornecedor(models.Model):
	nome = models.CharField(max_length=50)
	endereco = models.CharField(max_length=200)
	site = models.CharField(max_length=70)
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=2, choices=constants.STATE_CHOICES, blank=True)
	telefone = models.CharField(max_length=30)
	nome_contato = models.CharField(max_length=30)
	email_contato = models.CharField(max_length=50)
	
	def __str__(self):
		return u'%s' % (self.nome)

	class Meta:
		verbose_name = "Fornecedor"
		verbose_name_plural = "Fornecedores"
	

class NotaFiscal(models.Model):
	identificacao = models.CharField(max_length=50)
	fornecedor = models.ForeignKey(Fornecedor, models.SET_NULL, blank=True, null=True)
	nome = models.CharField(max_length=50)
	
	def __str__(self):
		return u'%s - %s ' % (self.identificacao, self.fornecedor)

	class Meta:
		verbose_name = "Nota Fiscal"
		verbose_name_plural = "Notas Fiscais"


class FuncaoFerramenta(models.Model):
	nome = models.CharField(max_length=50)
	
	def __str__(self):
		return u'%s' % (self.nome)

	class Meta:
		verbose_name = "Função da Ferramenta"
		verbose_name_plural = "Função das Ferramentas"


class Ferramenta(models.Model):
	nome = models.CharField(max_length=50)
	modelo = models.CharField(max_length=50)
	funcao_ferramenta = models.ForeignKey(FuncaoFerramenta, models.SET_NULL, blank=True, null=True,)
	descricao = models.CharField(max_length=200)
	apelido = models.CharField(max_length=30)
	fabricante = models.CharField(max_length=30)
	data_aquisicao = models.DateField()
	nota_fiscal = models.ForeignKey(NotaFiscal, models.SET_NULL, blank=True, null=True)
	fornecedor = models.ForeignKey(Fornecedor, models.SET_NULL, blank=True, null=True)
	foto = models.ImageField(upload_to='uploads/foto_ferramentas', blank=True)
	voltagem = models.CharField(max_length=30)
	amperagem = models.CharField(max_length=30)
	potencia = models.CharField(max_length=30)
	numero_controle = models.CharField(max_length=30)

	def __str__(self):
		return u'%s - %s' % (self.nome, self.fabricante)

	class Meta:
		verbose_name = "Ferramenta"
		verbose_name_plural = "Ferramentas"




