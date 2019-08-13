from django.contrib import admin
import requests
from django.urls import include, path
from django.conf.urls import url
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
import json, codecs
from django.shortcuts import render
from django.contrib import messages
import base64

from django import forms
from .models import Pacote, Contrato, PeriodosReservaRecurso, Regra
from contaazul.admin import TokenAdmin

# class TipoAssinaturaAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'periodo')
    
#     def changelist_view(self, request, extra_context=None):
#         extra_context = {'title': 'Lista dos tipos de assinatura'}
#         return super(TipoAssinaturaAdmin, self).changelist_view(request, extra_context=extra_context)


class PacoteAdmin(admin.ModelAdmin):
	search_fields = ['nome']
	filter_horizontal = ('regra', 'contrato', 'curso','outraAtividade')
    
	def save_model(self, request, obj, form, change):
		#Todo: tratar excecoes
		# tokenAdmin = TokenAdmin()
		token = TokenAdmin.atualizar_token()

		headers = TokenAdmin.set_authorization_header('bearer', token)
		# headers={'Authorization': 'Bearer %s' % token, "Content-Type": "application/json"}
		try:
			post_data = {"name": form.data['nome'], "value": form.data['valor_venda'], "cost": form.data['valor_custo'], "code": form.data['codigo']}
		except:
			return 'error'

		if form.data['id_contaazul']: #atualizando pacote
			response_content_json = TokenAdmin.request_contaazul('save_service', "https://api.contaazul.com/v1/services/%s" % form.data['id_contaazul'], None, json.dumps(post_data), headers)
			messages.success(request, response_content_json)
		else:
			#TODO: Colocar requests do conta AZUL em outro metodo (/contaazul)
			# response = requests.request(method="POST", url="https://api.contaazul.com/v1/services", data=json.dumps(post_data), headers=headers)
			# content = response.content
			# content_json = json.loads(content.decode("utf-8"))

			response_content_json = TokenAdmin.request_contaazul('update_service', "https://api.contaazul.com/v1/services", None, json.dumps(post_data), headers)

			_mutable = form.data._mutable
			form.data._mutable = True
			form.data['id_contaazul'] = response_content_json['id']
			obj.id_contaazul = response_content_json['id']
			form.data._mutable = _mutable
			#TODO: melhorar modelo de mensagens de resposta e excecoes
			messages.success(request, response_content_json)

		super(PacoteAdmin, self).save_model(request, obj, form, change)

class RegraAdmin(admin.ModelAdmin):
    filter_horizontal = ('recurso', 'periodosReservaRecurso')

admin.site.register(Pacote, PacoteAdmin)
admin.site.register(Contrato)
admin.site.register(PeriodosReservaRecurso)
admin.site.register(Regra, RegraAdmin)
