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

from .models import UsuarioEspaco


class UsuarioEspacoAdmin(admin.ModelAdmin):
	change_list_template = "admin/usuario_espaco/change_list.html"

	list_display = ('primeiro_nome', 'sobrenome', 'email', 'tipo_assinatura', 'restart_button')
	actions = ['record_rfid']
	# list_filter = ('tipo_assinatura','tipo_funcionario')

	def changelist_view(self, request, extra_context=None):
		extra_context = {'title': 'Lista de todos os usuários do espaço'}
		return super(UsuarioEspacoAdmin, self).changelist_view(request, extra_context=extra_context)
	
	def record_rfid(self, request, id_usuario):
		
		# return HttpResponseRedirect("")

		primeiro_nome = ""
		
		try:
			queryset = UsuarioEspaco.objects.get(id=id_usuario)
			primeiro_nome = " " + queryset.primeiro_nome
		except:
			primeiro_nome = ""
		

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
			# print(queryset.count());
			r = requests.get('http://192.168.20.3', headers={'id_usuario': str(id_usuario)})
			# url = reverse('admin:polls_choice_change', args=(c.id,))
			url = reverse(
                        'admin:usuarios_meviro_usuarioespaco_changelist',
                        # current_app=self.admin_site.name,
                        # args=(id_usuario,)
                    )

			messages.success(request, 'O comando foi enviado para gravadora de cartão. ID_Usuario: ' + str(id_usuario))

			return HttpResponseRedirect(url);

		return TemplateResponse(request, "admin/usuario_espaco/confirm_rfid_record.html")
		# print(queryset.count());
		# if queryset.count()==1:
		# 	print(">>>" + str(queryset[0].id))
		# 	r = requests.get('http://192.168.20.3', headers={'id_usuario': str(queryset[0].id)})
		# 	print(r)
	
	def get_urls(self):
		# use get_urls for easy adding of views to the admin
		urls = super(UsuarioEspacoAdmin, self).get_urls()
		my_urls = [path('record_rfid/<int:id_usuario>/', self.admin_site.admin_view(self.record_rfid), name='record_rfid'),]

		# url(r'^my_view/$', admin.site.admin_view(my_view))


		print(my_urls + urls)
		return my_urls + urls

	# def account_actions(self, obj):
	# 	return format_html(
	# 		'<a class="button" href="{}" style="color:#fff;">Deposit</a>',
	# 		reverse('admin:record_rfid', args=[obj.pk])
	# 	)
		

# def restart(self, request, id):
#     MyModel.objects.get(id=id).restart()
#     request.user.message_set.create(message="%s restarted." % id)
#     return http.HttpResponseRedirect('../')

	def record_rfidd(modeladmin, request, queryset, id):
		print("Gravando Cartão")

	# account_actions.short_description = 'Account Actions'
	# account_actions.allow_tags = True

	record_rfid.short_description = "Selecione o usuario para criar seu cartão"
	    
	    # print(response)

admin.site.site_header = "Espaço MeViro"
admin.site.site_title = "Gestão do Espaço MeViro"
admin.site.index_title = "Bem vindo ao sistema de controle do Espaço MeViro."

admin.site.register(UsuarioEspaco, UsuarioEspacoAdmin)
# admin.site.register(Avatar)



