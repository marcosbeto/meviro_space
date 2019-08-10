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
from administrativo.models import Pacote
from contaazul.admin import TokenAdmin


class UsuarioEspacoAdmin(admin.ModelAdmin):
	change_list_template = "admin/usuario_espaco/change_list.html"

	list_display = ('primeiro_nome', 'sobrenome', 'email', 'restart_button', 'refresh_pacotes')
	actions = ['record_rfid', 'atualizar_pacotes_usuario']
	search_fields = ['primeiro_nome', 'sobrenome', 'email']
	filter_horizontal = ('treinamentoEmEquipamentos', )

	def save_model(self, request, obj, form, change):
		print("form")
		print(form.data['primeiro_nome'])
		token = TokenAdmin.atualizar_token(None)

		headers={'Authorization': 'Bearer %s' % token, "Content-Type": "application/json"}
		post_data = {"name": form.data['primeiro_nome'], "person_type":"NATURAL"}
		
		if form.data['id_contaazul']:
			response = requests.request(method="PUT", url="https://api.contaazul.com/v1/customers/%s" % form.data['id_contaazul'], data=json.dumps(post_data), headers=headers)
			content = response.content
			messages.success(request, "Atualizando %s" % content)
		else:
			response = requests.request(method="POST", url="https://api.contaazul.com/v1/customers", data=json.dumps(post_data), headers=headers)
			content = response.content
			content_json = json.loads(content.decode("utf-8"))
			id_contaazul = content_json['id']
			_mutable = form.data._mutable
			form.data._mutable = True
			form.data['id_contaazul'] = id_contaazul
			obj.id_contaazul = id_contaazul
			form.data._mutable = _mutable
			messages.success(request, "Inserindo novo %s" % content)

		super(UsuarioEspacoAdmin, self).save_model(request, obj, form, change)
	
	def changelist_view(self, request, extra_context=None):
		extra_context = {'title': 'Lista de todos os usuários do espaço'}
		return super(UsuarioEspacoAdmin, self).changelist_view(request, extra_context=extra_context)
	
	def atualizar_pacotes_usuario(self, request, id_contaazul):

		token = TokenAdmin.atualizar_token(None)

		headers={'Authorization': 'Bearer %s' % token, "Content-Type": "application/json"}
		params = {"customer_id": id_contaazul, "status": "COMMITTED"}
		response = requests.request(method="GET", url="https://api.contaazul.com/v1/sales", params=params, headers=headers)
		all_sales = response.content
		all_sales_json = json.loads(all_sales.decode("utf-8"))
		
		message = ""

		for sale in all_sales_json:
			
			params_sale = {"id": sale['id']}
			response_sale = requests.request(method="GET", url="https://api.contaazul.com/v1/sales/%s/items" % sale['id'], params=params_sale, headers=headers)
			items_sale = response_sale.content
			items_sale_json = json.loads(items_sale.decode("utf-8"))
			
			array_id_pacotes_por_usuario = []

			for item in items_sale_json:
				id_pacote = json.dumps(item['item']['id']).strip('"')
				array_id_pacotes_por_usuario.append(id_pacote)
				

			PacotePorUsuarioAdmin.salvar_pacote_por_usuario_contaazul(id_contaazul, array_id_pacotes_por_usuario, sale['id'], sale['emission'])
		
		
		messages.success(request, "Lista %s" % message)
		url_base = reverse('admin:usuarios_meviro_usuarioespaco_changelist',)
		return HttpResponseRedirect(url_base);

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
			path('atualizar_pacotes_usuario/<str:id_contaazul>/', self.admin_site.admin_view(self.atualizar_pacotes_usuario), name='atualizar_pacotes_usuario'),
		]

		return my_urls + urls

	record_rfid.short_description = "Selecione o usuario para criar seu cartão"
	record_rfid.short_description = "Selecione o usuario para atualizar pacotes"

class AgendamentoAdmin(admin.ModelAdmin):
	autocomplete_fields = ('usuarios', 'recursos')

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
    actions = ['sincronizar_contaazul']

    def salvar_pacote_por_usuario_contaazul(id_contaazul, array_id_pacotes_por_usuario, id_venda, data_venda):
    	
    	for id_pacote_por_usuario in array_id_pacotes_por_usuario:
    		usuario_espaco = UsuarioEspaco.objects.get(id_contaazul=id_contaazul)
    		pacote = Pacote.objects.get(id_contaazul=id_pacote_por_usuario)
    		pacote_por_usuario_database = PacotePorUsuario.objects.filter(usuario__in=usuario_espaco, pacote__in=pacote, id_venda_contaazul=id_venda)
    		if not pacote_por_usuario_database:
    			pacote_por_usuario = PacotePorUsuario(usuario=usuario_espaco,pacote=pacote,ativo=False,data_ativacao=None,data_encerramento=None,id_venda_contaazul=id_venda)
    			pacote_por_usuario.save()

    def get_urls(self):
	    urls = super().get_urls()
	    my_urls = [
	        path('sincronizar_contaazul/', self.admin_site.admin_view(self.sincronizar_contaazul), name='sincronizar_contaazul'),
		]
	    
	    # print(request.GET.get('code'))
	    return my_urls + urls

   
    def sincronizar_contaazul(self, id_contaazul):

    	
		# 	response = requests.request(method="GET", url="https://api.contaazul.com/v1/services/%s" % form.data['id_contaazul'], data=json.dumps(post_data), headers=headers)
		# 	content = response.content
		# 	messages.success(request, "Atualizando pacote: %s" % content)
		# else:
		# 	response = requests.request(method="POST", url="https://api.contaazul.com/v1/services", data=json.dumps(post_data), headers=headers)
		# 	content = response.content
		# 	content_json = json.loads(content.decode("utf-8"))
		# 	id_contaazul = content_json['id']
		# 	_mutable = form.data._mutable
		# 	form.data._mutable = True
		# 	form.data['id_contaazul'] = id_contaazul
		# 	obj.id_contaazul = id_contaazul
		# 	form.data._mutable = _mutable
		# 	messages.success(request, "Inserindo novo pacote: %s" % content)


    	url = reverse('admin:%s_%s_changelist' % ('usuarios_meviro', 'pacoteporusuario'))
    	return HttpResponseRedirect(url)

    def changelist_view(self, request, extra_context=None):
	    
	    self.other_search_fields = {} 
	    
	    code = request.GET.get('code')
	    access_token = request.GET.get('access_token')
	    refresh_token = request.GET.get('refresh_token')

	    asf = self.advanced_search_form
	    extra_context = {'asf':asf}

	    request.GET._mutable=True

	    for key in asf.fields.keys():
	        try:
	            temp = request.GET.pop(key)
	        except KeyError:
	            pass 
	        else:
	            if temp!=['']: 
	                self.other_search_fields[key] = temp 

	    request.GET_mutable=False
	    extra_context = {'code': code, 'access_token': access_token, 'refresh_token': refresh_token} 

	    if (code):
	    	self.acessar_auth_token(request, code)

	    print("REQUEST:")
	    print(request)

	    return super(TokenAdmin, self).changelist_view(request, extra_context=extra_context)


#####





	    
admin.site.site_header = "Espaço MeViro"
admin.site.site_title = "Gestão do Espaço MeViro"
admin.site.index_title = "Sistema de administração do Espaço MeViro."

admin.site.register(UsuarioEspaco, UsuarioEspacoAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(PacotePorUsuario, PacotePorUsuarioAdmin)
admin.site.register(CreditoPorUsuario)




