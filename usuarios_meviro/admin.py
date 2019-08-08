# -*- coding: utf-8 -*-
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

from .models import UsuarioEspaco, Agendamento, PacotePorUsuario, CreditoPorUsuario
from contaazul.admin import TokenAdmin


class UsuarioEspacoAdmin(admin.ModelAdmin):
	change_list_template = "admin/usuario_espaco/change_list.html"

	list_display = ('primeiro_nome', 'sobrenome', 'email', 'restart_button')
	actions = ['record_rfid']
	search_fields = ['primeiro_nome', 'sobrenome', 'email']
	filter_horizontal = ('treinamentoEmEquipamentos', )

	def save_model(self, request, obj, form, change):
		print("form")
		print(form.data['primeiro_nome'])
		token = TokenAdmin.atualizar_token(None)

		headers={'Authorization': 'Bearer %s' % token, "Content-Type": "application/json"}
		post_data = {'name': form.data['primeiro_nome'], 'person_type':'NATURAL'}
		
		response = requests.request(method="POST", url="https://api.contaazul.com/v1/customers", params=post_data, headers=headers)
		content = response.content	

		messages.success(request, content)
		super(UsuarioEspacoAdmin, self).save_model(request, obj, form, change)
	
	def changelist_view(self, request, extra_context=None):
		extra_context = {'title': 'Lista de todos os usuários do espaço'}
		return super(UsuarioEspacoAdmin, self).changelist_view(request, extra_context=extra_context)
	
	def record_rfid(self, request, id_usuario):
		
		url_base = reverse('admin:usuarios_meviro_usuarioespaco_changelist',)

		try:
			queryset = UsuarioEspaco.objects.get(id=id_usuario)
			primeiro_nome = " " + queryset.primeiro_nome

			context = {
		        'opts': self.model._meta,
		        'app_label': self.model._meta.app_label, 
		        'primeiro_nome': primeiro_nome,
		        'change': False,
		        'add': False,
		        'is_popup': False,
		        'save_as': False,
		        'has_delete_permission': False,
		        'has_add_permission': False,
		        'has_change_permission': True,
		        'id_usuario': id_usuario
		    }

			if request.method != 'POST':
				return TemplateResponse(request, "admin/usuario_espaco/confirm_rfid_record.html", context)
			else:

				r = requests.get('http://192.168.20.7', headers={'id_usuario': str(id_usuario)})
				
				messages.success(request, 'O comando foi enviado para gravadora de cartão. ID_Usuario: ' + str(id_usuario))

				return HttpResponseRedirect(url_base);
		except:
			messages.error(request, 'Aconteceu algo de errado durante o processo de gravação do cartão.')
			return HttpResponseRedirect(url_base);
		
	def get_urls(self):
		# use get_urls for easy adding of views to the admin
		urls = super(UsuarioEspacoAdmin, self).get_urls()
		my_urls = [
			path('record_rfid/<int:id_usuario>/', self.admin_site.admin_view(self.record_rfid), name='record_rfid'),
		]

		return my_urls + urls

	record_rfid.short_description = "Selecione o usuario para criar seu cartão"

class AgendamentoAdmin(admin.ModelAdmin):
	autocomplete_fields = ('usuarios', 'recursos')


# class FormForAdvancedSearch(forms.Form):
#     #you can put any field here this is an example so only 1 simple CharField
#     code = forms.CharField()
#     state = forms.CharField()

# class PacotePorUsuarioAdmin(admin.ModelAdmin):
	
# 	change_list_template = "admin/administrativo/pacotes_por_usuario/change_list.html"
# 	code = ""
# 	search_fields = ['code','state']
# 	actions = ['sincronizar_pacotes_contaazul']
# 	other_search_fields = {}
# 	advanced_search_form = FormForAdvancedSearch()

# 	def sincronizar_pacotes_contaazul(self, request):
# 		print("eeeepaaaa")
# 		if request.method == 'GET':
# 			client_id = 'ivs1DUEHnAPyjOPDNyyG2bQiTlrPSsgs'
# 			client_key = 'FIOme5ZCQrHycctbadpGKsCFhhanc0dv'
# 			state_code = 'orivem'
# 			endpoint = 'https://api.contaazul.com/auth/authorize?redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&scope=sales&state={STATE}'
# 			url = endpoint.format(REDIRECT_URI='http://mevirospace.herokuapp.com/admin/usuarios_meviro/pacoteporusuario/', CLIENT_ID=client_id, STATE=state_code)
# 		return HttpResponseRedirect(url)


	def syncronize_contaazul(self, request):
		context = {
		        'opts': self.model._meta,
		        'app_label': self.model._meta.app_label, 
		        'change': False,
		        'add': False,
		        'is_popup': False,
		        'save_as': False,
		        'has_delete_permission': False,
		        'has_add_permission': False,
		        'has_change_permission': True,
		    }
		return TemplateResponse(request, "admin/auth_contaazul.html", context)

#####

class ActiveFilterForm(forms.Form):
    code = forms.CharField()
    state = forms.CharField()

class PacotePorUsuarioAdmin(admin.ModelAdmin): 

    advanced_search_form = ActiveFilterForm()
    change_list_template = "admin/administrativo/pacotes_por_usuario/change_list.html"
    actions = ['atualizar_token']

    def get_urls(self):
	    urls = super().get_urls()
	    my_urls = [
	        path('atualizar_token/', self.admin_site.admin_view(self.atualizar_token), name='atualizar_token'),
		]
	    
	    # print(request.GET.get('code'))
	    return my_urls + urls

   
    def atualizar_token(self, request):
    	token = TokenAdmin.atualizar_token(None)
    	url = reverse('admin:%s_%s_changelist' % ('usuarios_meviro', 'pacoteporusuario'))
    	messages.success(request, 'Token atualizado: %s' % token)
    	return HttpResponseRedirect(url)


#####





	    
admin.site.site_header = "Espaço MeViro"
admin.site.site_title = "Gestão do Espaço MeViro"
admin.site.index_title = "Sistema de administração do Espaço MeViro."

admin.site.register(UsuarioEspaco, UsuarioEspacoAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(PacotePorUsuario, PacotePorUsuarioAdmin)
admin.site.register(CreditoPorUsuario)




