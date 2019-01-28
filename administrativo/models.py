from django.db import models
from meviro_space import constants

# Create your models here.

class Assinatura(models.Model):
    nome = models.CharField(max_length=30)
    data_implantacao = models.DateField()
    ultima_atualizacao =  models.DateField(blank=True)
    valor = models.IntegerField(blank=True)
    periodo = models.CharField(max_length=30)
    observacao = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
    	return u'%s - %s' % (self.nome, self.periodo)

    class Meta:
    	verbose_name_plural = "Tipos de Assinatura"


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
	

