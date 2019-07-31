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

from .models import UsuarioEspaco, Agendamento, PacotePorUsuario, CreditoPorUsuario


class UsuarioEspacoAdmin(admin.ModelAdmin):
	change_list_template = "admin/usuario_espaco/change_list.html"

	list_display = ('primeiro_nome', 'sobrenome', 'email', 'restart_button')
	actions = ['record_rfid']
	search_fields = ['primeiro_nome', 'sobrenome', 'email']
	filter_horizontal = ('treinamentoEmEquipamentos', )
	
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
		my_urls = [path('record_rfid/<int:id_usuario>/', self.admin_site.admin_view(self.record_rfid), name='record_rfid'),]

		return my_urls + urls

	record_rfid.short_description = "Selecione o usuario para criar seu cartão"

class AgendamentoAdmin(admin.ModelAdmin):
	autocomplete_fields = ('usuarios', 'recursos')

class PacotePorUsuarioAdmin(admin.ModelAdmin):
	
	change_list_template = "admin/administrativo/pacotes_por_usuario/change_list.html"
	code = ""
	
	def changelist_view(self, request, extra_context=None):
		print("eeeeeeitaaaaaa")
		request.GET._mutable = True
		self.code = request.GET.get('code')
		print(self.code)
		request.GET.pop('code')

		extra_context = {'title': 'Lista de todos os usuários do espaço', 'code':self.code}
		return super(PacotePorUsuarioAdmin, self).changelist_view(request, extra_context=extra_context)
	
	# def changelist_view(self, request, *args, **kwargs):
	# 	# self.request = request
	# 	print("eeeeeeitaaaaaa")
	# 	# print(request.GET.get('code'))

	def get_urls(self):
	    urls = super().get_urls()
	    my_urls = [
	        path('sincronizar_pacotes_contaazul/', self.sincronizar_pacotes_contaazul),
	    ]
	    # print(request.GET.get('code'))
	    return my_urls + urls

	def sincronizar_pacotes_contaazul(self, request):
		print(request)
		reader = codecs.getreader("utf-8")
		if request.method == 'GET':
			client_id = 'ivs1DUEHnAPyjOPDNyyG2bQiTlrPSsgs'
			client_key = 'FIOme5ZCQrHycctbadpGKsCFhhanc0dv'
			state_code = 'orivem'
			endpoint = 'https://api.contaazul.com/auth/authorize?redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&scope=sales&state={STATE}'
			url = endpoint.format(REDIRECT_URI='http://mevirospace.herokuapp.com/admin/usuarios_meviro/pacoteporusuario/', CLIENT_ID=client_id, STATE=state_code)
			# headers = {}
			# print(url)
			# response = requests.get(url)
			# if response.status_code == 200:  # SUCCESS
			# 	result = response
			# 	print(type(response))
			# 	print(result.data)
			# 	data = json.load(reader(result))
			# 	print(data)
			# 	result['success'] = True
			# else:
			# 	result['success'] = False
			# 	if response.status_code == 404:  # NOT FOUND
			# 		result['message'] = 'No entry found for "%s"' % word
			# 	else:
			# 		result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
			# return result
		return HttpResponseRedirect(url)
		# return super(UsuarioEspacoAdmin, self).changelist_view(request, extra_context=extra_context)

	    
admin.site.site_header = "Espaço MeViro"
admin.site.site_title = "Gestão do Espaço MeViro"
admin.site.index_title = "Sistema de administração do Espaço MeViro."

admin.site.register(UsuarioEspaco, UsuarioEspacoAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(PacotePorUsuario, PacotePorUsuarioAdmin)
admin.site.register(CreditoPorUsuario)




