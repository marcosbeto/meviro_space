# -*- coding: utf-8 -*-
from django.db import models
from meviro_space import constants
from infra.models import Recurso
from django.contrib.postgres.fields import ArrayField

class TreinamentoEmEquipamento(models.Model):
	recurso = models.ManyToManyField(Recurso, verbose_name="Recurso utilizado no treinamento")

	def __str__(self):
		recurso_str = ""
		for recurso in self.recurso.all():
			recurso_str = recurso_str + "(" +recurso.nome + ") "
		return u'%s' % (recurso_str)

	class Meta:
		verbose_name = "Treinamento em Equipamento"
		verbose_name_plural = "Treinamentos em Equipamentos"
			
class Curso(models.Model):
	nome = models.CharField(max_length=30, verbose_name="Nome do Curso")
	descricao = models.TextField(verbose_name="Descrição do Curso", null=True)
	professores = models.TextField(verbose_name="Professores do Curso", null=True)
	precisa_treinamento = models.BooleanField(default=False, verbose_name="É necessário treinamento em equipamentos?")
	treinamentoEmEquipamentos = models.ManyToManyField(TreinamentoEmEquipamento, verbose_name="Em quais equipamentos?")
	dates = ArrayField(models.DateField(), verbose_name="Quais as datas do curso?")
	observacoes = models.TextField(verbose_name="Observações", null=True)

	def __str__(self):
		return u'%s' % (self.nome)

	class Meta:
		verbose_name = "Curso"
		verbose_name_plural = "Cursos"

class OutraAtividade(models.Model):
	nome = models.CharField(max_length=30, verbose_name="Nome da Atividade")
	descricao = models.TextField(verbose_name="Descrição da Atividade", null=True)
	organizadores = models.TextField(verbose_name="Organizadores da Atividade", null=True)
	treinamentoEmEquipamentos = models.ManyToManyField(TreinamentoEmEquipamento, verbose_name="Treinamento em Equipamentos")
	dates = ArrayField(models.DateField(),verbose_name="Quais as datas da atividade?")
	observacoes = models.TextField(verbose_name="Observações", null=True)

	def __str__(self):
		return u'%s - %s' % (self.nome, self.dates)

	class Meta:
		verbose_name = "Outra Atividade"
		verbose_name_plural = "Outras Atividades"

