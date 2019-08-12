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

class TokenAdmin(admin.ModelAdmin):
	search_fields = ['token']

	advanced_search_form = ActiveFilterForm()
	change_list_template = "admin/contaazul/token/change_list.html"
	actions = ['requisitar_autenticacao_inicial', 'atualizar_token']

	def get_urls(self):
		urls = super().get_urls()
		my_urls = [
			path('requisitar_autenticacao_inicial/', self.admin_site.admin_view(self.requisitar_autenticacao_inicial), name='requisitar_autenticacao_inicial'),
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
		token = self.atualizar_token()
		messages.success(request, 'Token atualizado: %s' % token)
		url = reverse('admin:%s_%s_changelist' % ('contaazul', 'token'))
		return HttpResponseRedirect(url)


	def set_authorization_header(self, type_authorization, token):
		headers = {}
		if type_authorization == 'basic':
			authorization_str = '{CLIENT_ID}:{CLIENT_KEY}'.format(CLIENT_ID=settings.CA_CLIENT_ID, CLIENT_KEY=settings.CA_CLIENT_KEY)
			headers={'Authorization': 'Basic %s' % base64.b64encode(authorization_str.encode('ascii')).decode("utf-8")}
		else:
			headers={'Authorization': 'Bearer %s' % token, "Content-Type": "application/json"}

		return headers


	def request_contaazul(self, type, url, params, data, headers):
		if type=='refresh_token':
			request_response = requests.request("POST", url, params=params, headers=headers)
		elif type=='authorization_code': 
			request_response = requests.request("POST", 'https://api.contaazul.com/oauth2/token/', params=params, headers=headers)

		token_content = request_response.content
		token_content_json = json.loads(token_content.decode("utf-8"))

		return token_content_json


	def set_authorization_request_data(self, type, token, code):
		data = {}
		if type == 'refresh_token':
			data = {'grant_type': 'refresh_token', 'refresh_token': current_refresh_token}
		elif type == 'authorization_code':
			data = {'grant_type': 'authorization_code', 'redirect_uri': settings.REDIRECT_URI , 'code': code}


		return data


	def atualizar_token(self):
		#TODO: tratar excessões
		headers = self.set_authorization_header('basic', None)
		
		#TODO: melhorar modelo de atualizacao
		token_obj = Token.objects.first()
		post_data = self.set_authorization_request_data('refresh_token', token_obj.refresh_token, None)
		token_content_json = request_contaazul('refresh_token','https://api.contaazul.com/oauth2/token/', post_data, None, headers)

		# response = requests.request("POST", 'https://api.contaazul.com/oauth2/token/', params=post_data, headers=headers)
		# token_content = response.content

		# token_content_json = json.loads(token_content.decode("utf-8"))

		access_token = token_content_json['access_token']
		refresh_token = token_content_json['refresh_token']
		
		#TODO: tratar exececoes

		token_obj_to_refresh = Token(token=access_token, refresh_token=refresh_token, hora_atualizacao=datetime.datetime.now())
		token_obj_to_refresh.save()

		return access_token


	def requisitar_autenticacao_inicial(self, request):
		#TODO: tratar excessões
		if request.method == 'GET':
			client_id = 'pPIYG4rGDP11A0CHTeanFTSLeGiZNGuE'
			state_code = 'orivem'
			endpoint = 'https://api.contaazul.com/auth/authorize?redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&scope=sales&state={STATE}'
			url = endpoint.format(REDIRECT_URI='https://mevirospace.herokuapp.com/admin/contaazul/token/', CLIENT_ID=client_id, STATE=state_code)
		return HttpResponseRedirect(url)


	def acessar_auth_token(self, request, code):
		#TODO: tratar excessões

		#BEGIN: PARTE REPLICADA EM OUTRO METODO
		# client_id = 'pPIYG4rGDP11A0CHTeanFTSLeGiZNGuE' #TODO: colocar no global
		# client_key = 'H3l6iIiNYgsYyjh6m5sWZ8WMoKL5rOBy'
		# to_encode = '{CLIENT_ID}:{CLIENT_KEY}'.format(CLIENT_ID=client_id, CLIENT_KEY=client_key)
		# encoded = base64.b64encode(to_encode.encode('ascii'))
		# headers={'Authorization': 'Basic %s' % encoded.decode("utf-8")}
		#END: PARTE REPLICADA EM OUTRO METODO

		headers = self.set_authorization_header('basic', None)

		# post_data = {'grant_type': 'authorization_code', 'redirect_uri': 'https://mevirospace.herokuapp.com/admin/contaazul/token/', 'code': code}

		post_data = self.set_authorization_request_data('authorization_code', None, token_obj.code)
		
		#TODO: colocar requisicoes ao Conta Azul em outro metodo
		# response = requests.request("POST", 'https://api.contaazul.com/oauth2/token/', params=post_data, headers=headers)

		token_content_json = request_contaazul('authorization_code','https://api.contaazul.com/oauth2/token/', post_data, None, headers)
		
		access_token = token_content_json['access_token']
		refresh_token = token_content_json['refresh_token']

		#TODO: tratar excessões
		token_object = Token(token=access_token, refresh_token=refresh_token, hora_atualizacao=datetime.datetime.now())
		token_object.save()
		messages.success(request, authorization_content_json)
		
		url = reverse('admin:%s_%s_changelist' % ('contaazul', 'token'))
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

	    return super(TokenAdmin, self).changelist_view(request, extra_context=extra_context)
	    

admin.site.register(Token, TokenAdmin)