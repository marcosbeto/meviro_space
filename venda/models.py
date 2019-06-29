from django.db import models
from usuarios_meviro.models import UsuarioEspaco
from administrativo.models import Pacote, Contrato

# Create your models here.
class OrdemDeServico(models.Model):
	
	STATUS_ORDEM = [
	    ('orcamento_pendente','Orçamento Pendente'),
	    ('servico_pendente','Serviço Pendente'),
	    ('em_andamento','Em andamento'),
	    ('concluido','Concluído'),
	]

	usuario_meviro = models.ForeignKey(UsuarioEspaco, on_delete=models.DO_NOTHING, verbose_name="Cliente")
	status_os = models.CharField(
        max_length=20,
        choices=STATUS_ORDEM,
        default='Orçamento Pendente',
        verbose_name="Status da OS"
    )
	numero_os = models.IntegerField(blank=True, null=True, verbose_name="Número da OS")
	data_inicio = models.DateField(verbose_name="Data de início", null=True)
	previsao_entrega =  models.DateField(blank=True, verbose_name="Previsão de entrega", null=True)
	descricao_servico = models.TextField(blank=True, verbose_name="Descrição do serviço a ser prestado", null=True)
	observacoes	= models.TextField(blank=True, verbose_name="Observações", null=True)


	def __str__(self):
		return u'%s - %s' % (self.numero_os - self.usuario_meviro.primeiro_nome)

	class Meta:
		verbose_name = "Ordem de Serviço"
		verbose_name_plural = "Ordens de Serviços"


class VendaPacotesPorUsuario(models.Model):

	STATUS = [
	    ('pagamento_pendente','Pagamento Pendente'),
	    ('ativo','Ativo'),
	    ('expirado','Expirado')
	]

	usuario_meviro = models.ForeignKey(UsuarioEspaco, on_delete=models.DO_NOTHING, verbose_name="Cliente")
	pacotes = models.ManyToManyField(Pacote, blank=True, verbose_name="Pacotes")
	data_assinatura =  models.DateField(blank=True, verbose_name="Data da Assinatura", null=True)
	contratos = models.ManyToManyField(Contrato, blank=True)
	numero_venda = models.IntegerField(blank=True, null=True, verbose_name="Número da Venda de Pacote")
	status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pagamento Pendente',
        verbose_name="Status"
    )

	def __str__(self):

		pacotes_str = "( 	"
		
		
		for pacote in self.pacotes.all():
			pacotes_str = pacotes_str + pacote.nome + " "
		pacotes_str = pacotes_str + ") "
		
		return u'%s - %s' % (self.usuario_meviro.primeiro_nome, pacotes_str)

	class Meta:
		verbose_name = "Venda de Pacote"
		verbose_name_plural = "Venda de Pacotes"

class VendaCreditos(models.Model):

	usuario_meviro = models.ForeignKey(UsuarioEspaco, on_delete=models.DO_NOTHING, verbose_name="Cliente")
	data_venda =  models.DateField(blank=True, verbose_name="Data da Venda", null=True)
	contratos = models.ManyToManyField(Contrato, blank=True)
	numero_venda = models.IntegerField(blank=True, null=True, verbose_name="Número da Venda de Crédito")
	numero_creditos = models.IntegerField(blank=True, null=True, default=0, verbose_name="Quantidade de Créditos")
	
	def __str__(self):

		return u'%s - Créditos: %s' % (self.usuario_meviro.primeiro_nome, self.creditos)

	class Meta:
		verbose_name = "Venda de Crédito"
		verbose_name_plural = "Venda de Créditos"