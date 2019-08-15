from django.contrib import admin
from .models import Token
from django import forms
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
from .models import Token
from django.conf import settings
import datetime



class ActiveFilterForm(forms.Form):
    code = forms.CharField()
    state = forms.CharField()

class InterfaceToken:

	def __init__(self):
		print("Starting InterfaceToken")

	def set_authorization_header(self, type_authorization, token):
		headers = {}
		if type_authorization == 'basic':
			authorization_str = '{CLIENT_ID}:{CLIENT_KEY}'.format(CLIENT_ID=settings.CA_CLIENT_ID, CLIENT_KEY=settings.CA_CLIENT_KEY)
			headers={'Authorization': 'Basic %s' % base64.b64encode(authorization_str.encode('ascii')).decode("utf-8")}
		elif type_authorization == 'bearer':
			headers={'Authorization': 'Bearer %s' % token, "Content-Type": "application/json"}

		return headers


	def set_authorization_request_data(self, type, token, code):
		data = {}
		if type == 'refresh_token':
			data = {'grant_type': 'refresh_token', 'refresh_token': token}
		elif type == 'authorization_code':
			data = {'grant_type': 'authorization_code', 'redirect_uri': settings.REDIRECT_URI , 'code': code}

		return data

	def request_contaazul(self, type, url, params, data, headers):
		if type=='refresh_token':
			try:
				request_response = requests.request("POST", url, params=params, headers=headers)
			except:
				return 'error'
		elif type=='authorization_code': 
			try:
				request_response = requests.request("POST", url, params=params, headers=headers)
			except:
				return 'error'
		elif type == 'save_service':
			try:
				# requests.request(method="PUT", url="https://api.contaazul.com/v1/services/%s" % form.data['id_contaazul'], data=json.dumps(post_data), headers=headers)
				request_response = requests.request("PUT", url, data=data, headers=headers)
			except:
				return 'error'
		elif type == 'update_service':
			try:
				request_response = requests.request("POST", url, data=data, headers=headers)
			except:
				return 'error'

		token_content_json = json.loads(request_response.content.decode("utf-8"))

		return token_content_json

	def atualizar_token(self):
		#TODO: tratar excessões
		try:
			token_obj = Token.objects.first()
		except:
			return 'error'

		post_data = self.set_authorization_request_data('refresh_token', token_obj.refresh_token, None)
		headers = self.set_authorization_header('basic', None)

		token_content_json = self.request_contaazul('refresh_token','https://api.contaazul.com/oauth2/token/', post_data, None, headers)
		
		#TODO: tratar exececoes
		try:
			token_obj_to_refresh = Token(token=token_content_json['access_token'], refresh_token=token_content_json['refresh_token'], hora_atualizacao=datetime.datetime.now())
			token_obj_to_refresh.save()
		except:
			return 'error'

		return token_content_json['access_token']

	def requisitar_autenticacao_inicial(self, request):
		#TODO: tratar excessões
		# try:
		if request.method == 'GET':
			endpoint = 'https://api.contaazul.com/auth/authorize?redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&scope=sales&state={STATE}'
			url = endpoint.format(REDIRECT_URI=settings.REDIRECT_URI, CLIENT_ID=settings.CA_CLIENT_ID, STATE=settings.CA_STATE_CODE)
			return HttpResponseRedirect(url)
		# 	else:
		# 		return 'error'	
		# except:
		# 	return 'error'


	def acessar_auth_token(self, request, code):
		post_data = self.set_authorization_request_data('authorization_code', None, code)
		headers = self.set_authorization_header('basic', None)

		token_content_json = self.request_contaazul('authorization_code','https://api.contaazul.com/oauth2/token/', post_data, None, headers)
		
		#TODO: tratar excessões
		try:
			token_object = Token(token=token_content_json['access_token'], refresh_token=token_content_json['refresh_token'], hora_atualizacao=datetime.datetime.now())
			token_object.save()
		except:
			return 'error'

		#TODO: melhorar sistema de mensagens
		messages.success(request, token_content_json)
		
		url = reverse('admin:%s_%s_changelist' % ('contaazul', 'token'))
		return HttpResponseRedirect(url)


class TokenAdmin(admin.ModelAdmin):
	search_fields = ['token']

	advanced_search_form = ActiveFilterForm()
	change_list_template = "admin/contaazul/token/change_list.html"
	actions = ['requisitar_autenticacao_inicial', 'atualizar_token']
	interfaceToken = InterfaceToken()
	
	def __init__(self,*args, **kwargs):
		super(TokenAdmin, self).__init__(*args, **kwargs)
		# self.atualizar_token()

	def get_urls(self):
		urls = super().get_urls()
		my_urls = [
			path('requisitar_autenticacao_inicial/', self.admin_site.admin_view(self.interfaceToken.requisitar_autenticacao_inicial), name='requisitar_autenticacao_inicial'),
			path('atualizar_token/', self.admin_site.admin_view(self.action_atualizar_token), name='atualizar_token'),
		]
	    
		return my_urls + urls

	#BEGIN: Metodos para tratamento de requisições

	def get_changelist(self, request, **kwargs):

	    from django.contrib.admin.views.main import ChangeList
	    code = self.other_search_fields.get('code',None)
	    
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

	#END: Metodos para tratamento de requisições

	def action_atualizar_token(self, request):
		#TODO: tratar excessões
		token = interfaceToken.atualizar_token()
		messages.success(request, 'Token atualizado: %s' % token)
		url = reverse('admin:%s_%s_changelist' % ('contaazul', 'token'))
		return HttpResponseRedirect(url)

	def changelist_view(self, request, extra_context=None):
	    self.other_search_fields = {} 
	    
	    try:
	    	code = request.GET.get('code')
	    	access_token = request.GET.get('access_token')
	    	refresh_token = request.GET.get('refresh_token')
	    except:
	    	return 'error'

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
	    	interfaceToken.acessar_auth_token(request, code)

	    return super(TokenAdmin, self).changelist_view(request, extra_context=extra_context)
	    

# 	    ass ListAdminMixin(object):
#     def __init__(self, model, admin_site):
#         self.list_display = [field.name for field in model._meta.fields]
#         super(ListAdminMixin, self).__init__(model, admin_site)

# models = apps.get_models()
# for model in models:
#     admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
#     try:
#         admin.site.register(model, admin_class)
#     except admin.sites.AlreadyRegistered:
#         pass

admin.site.register(Token, TokenAdmin)