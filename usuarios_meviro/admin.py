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

from django import forms

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

# 	def changelist_view(self, request, extra_context=None):
# 		self.code = request.GET.get('code')
# 		self.other_search_fields = {} 

# 		# extra_context = {'title': 'Lista de todos os usuários do espaço'}        
# 		# # we now need to remove the elements coming from the form
#   #       # and save in the other_search_fields dict but it's not allowed
#   #       # to do that in place so we need to temporary enable mutability ( I don't think     
#   #       # it will cause any complicance but maybe someone more exeprienced on how 
#   #       # QueryDict works could explain it better) 
# 		# request.GET._mutable=True
        
# 		# for key in asf.fields.keys():
# 		# 	try:
# 		# 		temp = request.GET.pop(key)
# 		# 	except KeyError:
# 		# 		pass # there is no field of the form in the dict so we don't remove it
# 		# 	else:
# 		# 		if temp!=['']: #there is a field but it's empty so it's useless
# 		# 			self.other_search_fields[key] = temp 
                
# 		# request.GET_mutable=False
		
# 		return super(PacotePorUsuarioAdmin, self).changelist_view(request, extra_context=extra_context)
	
# 	# def changelist_view(self, request, *args, **kwargs):
# 	# 	# self.request = request
# 	# 	print("eeeeeeitaaaaaa")
# 	# 	# print(request.GET.get('code'))

# 	def get_urls(self):
# 	    urls = super().get_urls()
# 	    my_urls = [
# 	        path('syncronize_contaazul/', self.admin_site.admin_view(self.syncronize_contaazul), name='syncronize_contaazul'),
# 		]
	    
# 	    # print(request.GET.get('code'))
# 	    return my_urls + urls

# 	def sincronizar_pacotes_contaazul(self, request):
# 		print(request)
# 		reader = codecs.getreader("utf-8")
# 		if request.method == 'GET':
# 			client_id = 'ivs1DUEHnAPyjOPDNyyG2bQiTlrPSsgs'
# 			client_key = 'FIOme5ZCQrHycctbadpGKsCFhhanc0dv'
# 			state_code = 'orivem'
# 			endpoint = 'https://api.contaazul.com/auth/authorize?redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&scope=sales&state={STATE}'
# 			url = endpoint.format(REDIRECT_URI='http://mevirospace.herokuapp.com/admin/usuarios_meviro/pacoteporusuario/', CLIENT_ID=client_id, STATE=state_code)
# 		return HttpResponseRedirect(url)
# 		# return super(UsuarioEspacoAdmin, self).changelist_view(request, extra_context=extra_context)


# # you need a templatetag to rewrite the standard search_form tag because the default   
# # templatetag to render the search form doesn't handle context so here it is:
# # remember to put it inside a source file (in my case is custom_search_form.py) that  
# # lives in project/myapp/templatetags otherwise will not be found by the template engine 

# from django.contrib.admin.views.main import SEARCH_VAR

# from django.template import Library

# register = Library()

# @register.inclusion_tag('admin/usuarios_meviro/pacoteporusuario/search_form.html', takes_context=True)
# def advanced_search_form(context, cl):
#     """
#     Displays a search form for searching the list.
#     """
#     return {
#         'asf' : context.get('asf'),
#         'cl': cl,
#         'show_result_count': cl.result_count != cl.full_result_count,
#         'search_var': SEARCH_VAR
#     }







#####

class ActiveFilterForm(forms.Form):
    code = forms.CharField()
    state = forms.CharField()

class PacotePorUsuarioAdmin(admin.ModelAdmin): 

    advanced_search_form = ActiveFilterForm()
    change_list_template = "admin/administrativo/pacotes_por_usuario/change_list.html"
    actions = ['sincronizar_pacotes_contaazul', 'acessar_auth_token']

    def get_urls(self):
	    urls = super().get_urls()
	    my_urls = [
	        path('sincronizar_pacotes_contaazul/', self.admin_site.admin_view(self.sincronizar_pacotes_contaazul), name='sincronizar_pacotes_contaazul'),
		]
	    
	    # print(request.GET.get('code'))
	    return my_urls + urls

    def get_changelist(self, request, **kwargs):

        from django.contrib.admin.views.main import ChangeList
        code = self.other_search_fields.get('code',None)
        # now we have the active_pp parameter that was passed in and can use it.

        class ActiveChangeList(ChangeList):

            def get_query_set(self, *args, **kwargs):
                now = datetime.datetime.now()
                qs = super(ActiveChangeList, self).get_query_set(*args, **kwargs)
                return qs.filter((Q(start_date=None) | Q(start_date__lte=now))
                                 & (Q(end_date=None) | Q(end_date__gte=now)))

        if not code is None:
            return ActiveChangeList

        return ChangeList


    def lookup_allowed(self, lookup):
        if lookup in self.advanced_search_form.fields.keys():
            return True
        return super(MyModelAdmin, self).lookup_allowed(lookup)

    def sincronizar_pacotes_contaazul(self, request):
    	if request.method == 'GET':
    		client_id = 'ivs1DUEHnAPyjOPDNyyG2bQiTlrPSsgs'
    		client_key = 'FIOme5ZCQrHycctbadpGKsCFhhanc0dv'
    		state_code = 'orivem'
    		endpoint = 'https://api.contaazul.com/auth/authorize?redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&scope=sales&state={STATE}'
    		url = endpoint.format(REDIRECT_URI='http://mevirospace.herokuapp.com/admin/usuarios_meviro/pacoteporusuario/', CLIENT_ID=client_id, STATE=state_code)
    	return HttpResponseRedirect(url)
   
    def acessar_auth_token(self, request):
    	post_data = {'grant_type': 'authorization_code', 'redirect_uri': 'http://mevirospace.herokuapp.com/admin/usuarios_meviro/pacoteporusuario', 'code': '4fz1G4AooaXkR5DdH0oB3aTTQyNr3s9O'}
    	response = requests.post('https://api.contaazul.com/oauth2/token', data=post_data)
    	content = response.content
    	extra_context = {'code': code, 'access_token': content}
    	return super(PacotePorUsuarioAdmin, self).changelist_view(request, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None, **kwargs):
        self.other_search_fields = {} 
        code = request.GET.get('code')
        access_token = request.GET.get('access_token')
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
        extra_context = {'code': code, 'access_token': access_token}
        return super(PacotePorUsuarioAdmin, self).changelist_view(request, extra_context=extra_context)
        # return super(PacotePorUsuarioAdmin, self)\
               # .changelist_view(request, extra_context=extra_context)

#####





	    
admin.site.site_header = "Espaço MeViro"
admin.site.site_title = "Gestão do Espaço MeViro"
admin.site.index_title = "Sistema de administração do Espaço MeViro."

admin.site.register(UsuarioEspaco, UsuarioEspacoAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(PacotePorUsuario, PacotePorUsuarioAdmin)
admin.site.register(CreditoPorUsuario)




