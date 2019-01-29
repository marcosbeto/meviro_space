# -*- coding: utf-8 -*-
from django.contrib import admin
import requests

from .models import UsuarioEspaco


class UsuarioEspacoAdmin(admin.ModelAdmin):
	list_display = ('primeiro_nome', 'sobrenome', 'email', 'tipo_assinatura')
	actions = ['record_rfid']
	# list_filter = ('tipo_assinatura','tipo_funcionario')

	change_list_template = "admin/usuario_espaco/change_list.html"

	def changelist_view(self, request, extra_context=None):
		extra_context = {'title': 'Lista de todos os usuários do espaço'}
		return super(UsuarioEspacoAdmin, self).changelist_view(request, extra_context=extra_context)
	
	def record_rfid(modeladmin, request, queryset):
		print(queryset.count());
		if queryset.count()==1:
			print(">>>" + str(queryset[0].id))
			r = requests.get('http://192.168.20.3', headers={'id_usuario': str(queryset[0].id)})
			print(r)
			# opener = urllib.request.build_opener(urllib.HTTPHandler)
			# data = {}
			# request = urllib.Request('192.168.20.3', data=json.dumps(data))
			# request.add_header("Content-Type", "application/json") #Header, Valu
			# request.add_header("id_usuario", queryset[0].id) #Header, Valu

	    	# response = requests.get('192.168.20.3')
	    	# request.add_header("Content-Type", "application/json") #Header, Value                                        
			# opener.open(request)

	record_rfid.short_description = "Selecione o usuario para criar seu cartão"
	    
	    # print(response)

admin.site.site_header = "Espaço MeViro"
admin.site.site_title = "Gestão do Espaço MeViro"
admin.site.index_title = "Bem vindo ao sistema de controle do Espaço MeViro."

admin.site.register(UsuarioEspaco, UsuarioEspacoAdmin)
# admin.site.register(Avatar)



