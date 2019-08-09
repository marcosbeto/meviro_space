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
		
		token = TokenAdmin.atualizar_token(None)

		headers={'Authorization': 'Bearer %s' % token, "Content-Type": "application/json"}
		post_data = { "name": form.data['nome'], "value": form.data['valor_venda'], "cost": form.data['valor_custo'] }

		if form.data['id_contaazul']:
			response = requests.request(method="PUT", url="https://api.contaazul.com/v1/services/%s" % form.data['id_contaazul'], data=json.dumps(post_data), headers=headers)
			content = response.content
			messages.success(request, "Atualizando pacote: %s" % content)
		else:
			response = requests.request(method="POST", url="https://api.contaazul.com/v1/services", data=json.dumps(post_data), headers=headers)
			content = response.content
			content_json = json.loads(content.decode("utf-8"))
			id_contaazul = content_json['id']
			_mutable = form.data._mutable
			form.data._mutable = True
			form.data['id_contaazul'] = id_contaazul
			obj.id_contaazul = id_contaazul
			form.data._mutable = _mutable
			messages.success(request, "Inserindo novo pacote: %s" % content)

		super(PacoteAdmin, self).save_model(request, obj, form, change)

class RegraAdmin(admin.ModelAdmin):
    filter_horizontal = ('recurso', 'periodosReservaRecurso')

admin.site.register(Pacote, PacoteAdmin)
admin.site.register(Contrato)
admin.site.register(PeriodosReservaRecurso)
admin.site.register(Regra, RegraAdmin)
