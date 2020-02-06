# -*- coding: utf-8 -*-
from django.db import models
from meviro_space import constants
from infra.models import Recurso, Fornecedor
from educacao.models import Curso, OutraAtividade

class Contrato(models.Model):
	nome = models.CharField(max_length=30, verbose_name="Nome do Contrato")
	arquivo = models.ImageField(upload_to='arquivos/contratos', verbose_name="Arquivo do Contrato")
	descricao = models.TextField(null=True, verbose_name="Descrição")

	def __str__(self):
		return u'%s' % (self.nome)

	class Meta:
		verbose_name = "Contrato"
		verbose_name_plural = "Contratos"


class PeriodosReservaRecurso(models.Model): #verificar se não é melhor um array de opcoes
	periodo = models.CharField(max_length=30)

	def __str__(self):
		return u'%s' % (self.periodo)

	class Meta:
		verbose_name = "Período para Reseva"
		verbose_name_plural = "Períodos para Resevas"


class Regra(models.Model):
	recurso = models.ManyToManyField(Recurso, verbose_name="Garante acesso ao seguinte recurso:")
	periodosReservaRecurso = models.ManyToManyField(PeriodosReservaRecurso, verbose_name="Quando?") #verificar se não é melhor um array de opcoes

	def __str__(self):
		
		recurso_str = ""
		periodosReservaRecurso_str = ""
		
		for recurso in self.recurso.all():
			recurso_str = recurso_str + "(" +recurso.nome + ") "
		
		for periodosReservaRecurso in self.periodosReservaRecurso.all():
			periodosReservaRecurso_str = periodosReservaRecurso_str + "(" + periodosReservaRecurso.periodo + ") "
		

		return u'%s - %s' % (recurso_str, periodosReservaRecurso_str)

	class Meta:
		verbose_name = "Regra de Uso"
		verbose_name_plural = "Regras de Uso (Máquina por Período)"

class Servico(models.Model):
	nome = models.CharField(max_length=254, verbose_name="Nome do Serviço")

class OutrosProdutos(models.Model):
	nome = models.CharField(max_length=60, verbose_name="Nome do Produto")

class Pacote(models.Model):
	nome = models.CharField(max_length=60, verbose_name="Nome do Pacote", help_text="Pacote de Assinaturas, Cursos ou Outras Atividades.")
	valor_venda = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Valor de Venda")
	valor_custo = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Valor de Custo")
	codigo = models.CharField(max_length=50, blank=True, null=True, verbose_name="Código", default="MV_ADMIN")	

	descricao = models.TextField(verbose_name="Descrição do Pacote", null=True)
	data_implantacao = models.DateField(verbose_name="Data da Implantação", null=True)
	ultima_atualizacao =  models.DateField(blank=True, verbose_name="Data da Última Atualização", null=True)
	
	regra = models.ManyToManyField(Regra, verbose_name="Regras para utilização de recursos")
	numero_credito = models.IntegerField(blank=True, null=True, verbose_name="Número de créditos disponíveis")

	tipo_periodo_minimo = models.CharField(max_length=256, null=True, verbose_name="Período Mínimo", help_text="Dias, Semanas, Meses", blank=True, choices=[('Horas', 'horas'), ('Dias', 'dias'), ('Semanas', 'semanas'), ('Meses', 'meses')])
	valor_periodo_minimo = models.IntegerField(blank=True, null=True, verbose_name="Quantidade Período Mínimo")

	observacoes	= models.TextField(blank=True, verbose_name="Observações", null=True)

	pode_agendar_maquinas = models.BooleanField(default=False, verbose_name="Pode realizar agendamentos?",)
	is_responsavel = models.BooleanField(default=False, verbose_name="É responsável por alguém que usara o espaço?",)
	responsavel_por = models.CharField(max_length=256, null=True, verbose_name="Reponsável por", blank=True,)

	assinantes_tem_desconto_recurso = models.BooleanField(default=False, verbose_name="Assinantes tem desconto para utilização dos recursos?",)
	desconto_recurso_percentual = models.IntegerField(blank=True, null=True, verbose_name="Desconto percentual por recurso")
	desconto_recurso_valor = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=2, verbose_name="Desconto integral por recurso")

	contrato = models.ManyToManyField(Contrato, verbose_name="Contratos", blank=True)
	curso = models.ManyToManyField(Curso, verbose_name="Algum curso relacionado?", blank=True)
	outraAtividade = models.ManyToManyField(OutraAtividade, verbose_name="Alguma outra atividade relacionada?", blank=True)
	id_contaazul = models.CharField(max_length=200, blank=True, null=True, verbose_name="ID Conta Azul")
	
	def __str__(self):
		return u'%s' % (self.nome)

	class Meta:
		verbose_name = "Pacote"
		verbose_name_plural = "Pacotes"