# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from meviro_space import constants
from administrativo.models import Pacote, Contrato
from infra.models import Recurso
from educacao.models import TreinamentoEmEquipamento
from multiselectfield import MultiSelectField


class UsuarioEspaco(models.Model):
	
	PARA_QUEM_CONSTRUIR = [
	    ('propria', 'Para o próprio usuário.'),
	    ('contratante', 'Para um contratante'),
	    ('empregador', 'Para um empregador '),
		('outros', 'Outros')
	]

	RAZAO_VISITA = [
	    ('reuniao', 'Reunião'),
		('tour_agendado', 'Tour Agendado'),
		('tour_nao_agendado', 'Tour não agendado'),
		('visita_parceiro', 'Visita Parceiro'),
		('curso_atividade', 'Participar de uma Atividade'),
		('atividade_terceiros', 'Atividade de Terceiros'),
		('visita_parceiro', 'Visita Parceiro'),
		( 'uso_maquinas', 'Uso do Espaço'),
		('outros', 'Outros')
	]

	TODOS_INTERESSES = (('marcenaria', 'Marcenaria'),
              ('eletronica', 'Eletrônica'),
              ('impressao3D', 'Impressão 3D'),
              ('serralheria', 'Serralheria'),
              ('cortadora_laser', 'Cortarora Laser'),
              ('cnc', 'CNC'),
              ('cultura_maker', 'Cultura Maker'),
              ('atividades_impacto', 'Atividades de Impacto Socio Ambiental'),
              ('inclusao_pcds', 'Inclusão de PCDs'))

	primeiro_nome = models.CharField(max_length=30, verbose_name="Primeiro nome")
	sobrenome = models.CharField(max_length=200, verbose_name="Sobrenomes")
	razao_visita = models.CharField(max_length=30, choices=RAZAO_VISITA, null=True, verbose_name="Razão da Visita")
	cpf = models.CharField(max_length=30, verbose_name="CPF")
	rg = models.CharField(max_length=30, blank=True, null=True, verbose_name="RG")
	data_nascimento = models.DateField(verbose_name="Data de Nascimento")
	email = models.EmailField(max_length=50, verbose_name="E-mail")
	
	interesse_educador = models.BooleanField(default=False, verbose_name="Tem interesse em ser educador no espaço")
	possivel_parceiro_pf = models.BooleanField(default=False, verbose_name="Possível parceiro Pessoa Física")
	possivel_parceiro_pj = models.BooleanField(default=False, verbose_name="Possível parceiro Pessoa Jurídica")

	interesses = MultiSelectField(choices=TODOS_INTERESSES, default=None, blank=True, null=True, verbose_name="Interesses")
	habilidades = models.TextField(blank=True, verbose_name="Habilidades", null=True)
	indicacao_servicos = models.BooleanField(default=False, verbose_name="Gostaria de receber indicações para prestação de serviços")

	ocupacao_funcao = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ocupação Profissional")
	onde_trabalha = models.CharField(max_length=200, blank=True, null=True, verbose_name="Onde Trabalha")
	para_quem_construir = models.CharField(max_length=90, choices=PARA_QUEM_CONSTRUIR, blank=True, null=True, verbose_name="Para quem costuma construir?")
	
	treinamentoEmEquipamentos = models.ManyToManyField(TreinamentoEmEquipamento, blank=True, verbose_name="Possui treinamento nos seguintes equipamentos")

	outras_informacoes = models.TextField(blank=True, verbose_name="Outras informações relevantes", null=True)


	endereco = models.CharField(max_length=200, blank=True, null=True, verbose_name="Endereço")
	cidade = models.CharField(max_length=30, blank=True, null=True, verbose_name="Cidade")
	estado = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado", choices=constants.STATE_CHOICES)

	telefone_celular = models.CharField(max_length=30, blank=True, null=True)
	nome_contato_emergencia = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nome do Contato de Emergência")
	telefone_contato_emergencia = models.CharField(max_length=30, blank=True, verbose_name="Telefone do Contato de Emergência")
		
	foto = models.ImageField(upload_to='fotos_usuarios_espaco', blank=True, verbose_name="Foto do usuário")
	apelido = models.CharField(max_length=30, blank=True, null=True)
	
	tem_plano_saude = models.BooleanField(default=False, verbose_name="Usuário possui plano de saúde")
	nome_plano_saude = models.CharField(max_length=50, blank=True, null=True, verbose_name="Qual o nome do plano de saúde?")
	id_contaazul = models.CharField(max_length=200, blank=True, null=True, verbose_name="ID Conta Azul")

	
	def refresh_pacotes(self):
		return mark_safe("<a href='atualizar_pacotes_usuario/" + str(self.id_contaazul) + "/' style='background-color: #a6eaff;padding: 4px 8px;color: #333333;border-radius: 2px;font-weight: bold;font-size: 10pt;'>Atualizar Pacotes</a>")
    
	refresh_pacotes.allow_tags = True
	refresh_pacotes.short_description = "Atualizar Pacotes"

	def restart_button(self):
		return mark_safe("<a href='record_rfid/" + str(self.id) + "/' style='background-color: #ffcd00;padding: 4px 8px;color: #333333;border-radius: 2px;font-weight: bold;font-size: 10pt;'>Enviar comando</a>")
    
	restart_button.allow_tags = True
	restart_button.short_description = "Gravar Cartão"

	def __str__(self):
		return u'%s %s' % (self.primeiro_nome, self.sobrenome)

	class Meta:
		verbose_name_plural = "Usuários do Espaço"
		verbose_name = "Usuário do Espaço"
		 

class PacotePorUsuario(models.Model):
	usuario = models.ForeignKey(UsuarioEspaco, verbose_name="Nome do Usuário", on_delete=models.CASCADE)
	pacote = models.ForeignKey(Pacote, 	verbose_name="Pacote", on_delete=models.CASCADE)
	ativo = models.BooleanField(default=False, verbose_name="Este plano está ativo?")
	data_ativacao = models.DateField(blank=True, null=True, verbose_name="Data de Ativação")
	data_encerramento = models.DateField(blank=True, null=True, verbose_name="Data de Encerramento")
	id_venda_contaazul = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Venda ContaAzul")
	quantidade = models.IntegerField(blank=True, null=True, verbose_name="Quantidade")

	def __str__(self):
		return u'%s contratou  %s' % (self.usuario.primeiro_nome, self.pacote.nome)

	class Meta:
		verbose_name_plural = "Pacotes por Usuário"
		verbose_name = "Pacote por Usuário"

class CreditoPorUsuario(models.Model):
	usuario = models.ForeignKey(UsuarioEspaco, on_delete=models.CASCADE, verbose_name="Nome do Usuário")
	numero_creditos = models.ForeignKey(Pacote, on_delete=models.CASCADE, verbose_name="Pacote")
	is_active = models.BooleanField(default=False, verbose_name="Este plano está ativo?")
	data_compra = models.DateField(blank=True, null=True, verbose_name="Data de Ativação")
	data_encerramento = models.DateField(blank=True, null=True, verbose_name="Data de Encerramento")
	id_venda_contaazul = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Venda ContaAzul")

	class Meta:
		verbose_name_plural = "Créditos por Usuário"
		verbose_name = "Crédito por Usuário"


class Agendamento(models.Model):

	TIMES_CHOICES = [
	    ('10:00-11:00', '10:00:00-11:00:00'),
	    ('13:00-14:00', '13:00:00-14:00:00'),
	    ('17:00-18:00', '17:00:00-18:00:00'),
	    ('19:00-20:00', '19:00:00-20:00:00'),
	]

	usuarios = models.ForeignKey(UsuarioEspaco, on_delete=models.DO_NOTHING, verbose_name="Nome do Usuário")
	recursos = models.ForeignKey(Recurso, on_delete=models.DO_NOTHING, verbose_name="Recurso a ser reservado")
	data = models.DateField(verbose_name="Data para Reserva")
	horario = models.CharField(
        max_length=12,
        choices=TIMES_CHOICES,
        default='10:00-11:00',
        verbose_name="Horário da reserva"
    )
