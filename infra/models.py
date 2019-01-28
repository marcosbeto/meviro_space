# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from meviro_space import constants
from financeiro.models import NotaFiscal
from usuarios_meviro.models import UsuarioEspaco
from administrativo.models import Fornecedor

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
	fabricante = models.CharField(max_length=30)
	data_aquisicao = models.DateField()
	nota_fiscal = models.ForeignKey(NotaFiscal, models.SET_NULL, blank=True, null=True)
	fornecedor = models.ForeignKey(Fornecedor, models.SET_NULL, blank=True, null=True)
	foto = models.ImageField(upload_to='uploads/foto_ferramentas', blank=True)
	ferramenta_eletrica = models.BooleanField(default=True)
	voltagem = models.CharField(max_length=30, blank=True)
	amperagem = models.CharField(max_length=30, blank=True)
	potencia = models.CharField(max_length=30, blank=True)
	secao = models.ForeignKey(Secao, models.SET_NULL, blank=True, null=True)
	# numero_controle = models.CharField(max_length=30)

	def __str__(self):
		return u'%s - %s' % (self.nome, self.fabricante)

	class Meta:
		verbose_name = "Ferramenta"
		verbose_name_plural = "Ferramentas"

class Maquina(models.Model):
	nome = models.CharField(max_length=50)
	modelo = models.CharField(max_length=50)
	funcao_ferramenta = models.ForeignKey(FuncaoFerramenta, models.SET_NULL, blank=True, null=True,)
	apelido = models.CharField(max_length=20)
	descricao = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=30)
	data_aquisicao = models.DateField()
	data_ultima_manutencao = models.DateField()
	descricao_ultima_manutencao = models.TextField(null=True)
	nota_fiscal = models.ForeignKey(NotaFiscal, models.SET_NULL, blank=True, null=True)
	fornecedor = models.ForeignKey(Fornecedor, models.SET_NULL, blank=True, null=True)
	foto = models.ImageField(upload_to='uploads/foto_ferramentas', blank=True)
	voltagem = models.CharField(max_length=30)
	amperagem = models.CharField(max_length=30)
	potencia = models.CharField(max_length=30)
	secao = models.ForeignKey(Secao, models.SET_NULL, blank=True, null=True)
	# numero_controle = models.CharField(max_length=30)

	def __str__(self):
		return u'%s - %s' % (self.nome, self.fabricante)

	class Meta:
		verbose_name = "Ferramenta"
		verbose_name_plural = "Ferramentas"


class Arduino(models.Model):
	nome =  models.CharField(max_length=30, blank=True)
	codigo =  models.CharField(max_length=30, blank=True)

	def __str__(self):
		return u'%s' % (self.nome)
	
	class Meta:
		verbose_name = "Arduino"
		verbose_name_plural = "Arduinos"


class ArduinoAuth(models.Model):
	id_arduino = models.ForeignKey(UsuarioEspaco, blank=True, null=True, on_delete=models.DO_NOTHING)
	id_secao = models.ForeignKey(Secao, blank=True, null=True, on_delete=models.DO_NOTHING)
	
	def __str__(self):
		return u'%s [%s]' % (self.id_arduino, self.id_secao.nome)
	
	class Meta:
		verbose_name = "Arduino Auth"
		verbose_name_plural = "Arduinos Auth"




