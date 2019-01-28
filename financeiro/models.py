from django.db import models
from administrativo.models import Fornecedor

# Create your models here.
class NotaFiscal(models.Model):
	identificacao = models.CharField(max_length=50)
	fornecedor = models.ForeignKey(Fornecedor, models.SET_NULL, blank=True, null=True)
	nome = models.CharField(max_length=50)
	
	def __str__(self):
		return u'%s - %s ' % (self.identificacao, self.fornecedor)

	class Meta:
		verbose_name = "Nota Fiscal"
		verbose_name_plural = "Notas Fiscais"
