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
import datetime


class ActiveFilterForm(forms.Form):
    code = forms.CharField()
    state = forms.CharField()

class TokenAdmin(admin.ModelAdmin):
	search_fields = ['token']

	advanced_search_form = ActiveFilterForm()
	change_list_template = "admin/contaazul/token/change_list.html"
	actions = ['requisitar_autenticacao_inicial', 'acessar_auth_token', 'atualizar_token']

	def get_urls(self):
		urls = super().get_urls()
		my_urls = [
			path('requisitar_autenticacao_inicial/', self.admin_site.admin_view(self.requisitar_autenticacao_inicial), name='requisitar_autenticacao_inicial'),
			path('acessar_auth_token/', self.admin_site.admin_view(self.acessar_auth_token), name='acessar_auth_token'),
			path('atualizar_token/', self.admin_site.admin_view(self.atualizar_token), name='atualizar_token'),
		]
	    
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

	def atualizar_token(self, request):
		client_id = 'pPIYG4rGDP11A0CHTeanFTSLeGiZNGuE'
		client_key = 'H3l6iIiNYgsYyjh6m5sWZ8WMoKL5rOBy'
		to_encode = '{CLIENT_ID}:{CLIENT_KEY}'.format(CLIENT_ID=client_id, CLIENT_KEY=client_key)
		encoded = base64.b64encode(to_encode.encode('ascii'))
		headers={'Authorization': 'Basic %s' % encoded.decode("utf-8")}
		post_data = {'grant_type': 'refresh_token', 'refresh_token': 'bn54v9fZ8lL9DgRdNRjasbfVwUYBGJLL'}
		response = requests.request("POST", 'https://api.contaazul.com/oauth2/token/', params=post_data, headers=headers)
		# requests.request("POST", url, headers=headers, params=querystring)
		content = response.content
		content_json = json.loads(content.decode("utf-8"))

		# access_token = content_json['access_token']
		# refresh_token = content_json['refresh_token']
		# Token.objects.filter(pk=1).update(token=access_token, refresh_token=refresh_token, hora_atualizacao=datetime.datetime.now())
		
		print("CONTEEEEEENT")
		print(response.text)
		url = reverse('admin:%s_%s_changelist' % ('contaazul', 'token'))
		messages.success(request, json.loads(content.decode("utf-8")))
		return HttpResponseRedirect(url)

	def requisitar_autenticacao_inicial(self, request):
		if request.method == 'GET':
			client_id = 'pPIYG4rGDP11A0CHTeanFTSLeGiZNGuE'
			state_code = 'orivem'
			endpoint = 'https://api.contaazul.com/auth/authorize?redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&scope=sales&state={STATE}'
			url = endpoint.format(REDIRECT_URI='https://mevirospace.herokuapp.com/admin/contaazul/token/', CLIENT_ID=client_id, STATE=state_code)
		return HttpResponseRedirect(url)

	def acessar_auth_token(self, request, code):
		client_id = 'pPIYG4rGDP11A0CHTeanFTSLeGiZNGuE'
		client_key = 'H3l6iIiNYgsYyjh6m5sWZ8WMoKL5rOBy'
		to_encode = '{CLIENT_ID}:{CLIENT_KEY}'.format(CLIENT_ID=client_id, CLIENT_KEY=client_key)
		encoded = base64.b64encode(to_encode.encode('ascii'))
		headers={'Authorization': 'Basic %s' % encoded.decode("utf-8")}
		post_data = {'grant_type': 'authorization_code', 'redirect_uri': 'https://mevirospace.herokuapp.com/admin/contaazul/token/', 'code': code}
		response = requests.request("POST", 'https://api.contaazul.com/oauth2/token/', params=post_data, headers=headers)
		# requests.request("POST", url, headers=headers, params=querystring)
		content = response.content
		content_json = json.loads(content.decode("utf-8"))

		access_token = content_json['access_token']
		refresh_token = content_json['refresh_token']

		token_object = Token(token=access_token, refresh_token=refresh_token, hora_atualizacao=datetime.datetime.now())
		token_object.save()

		print("CONTEEEEEENT")
		print(response.text)
		extra_context = {'access_token': '123'}
		url = reverse('admin:%s_%s_changelist' % ('contaazul', 'token'))
		messages.success(request, content_json)
		return HttpResponseRedirect(url)
		# return super(PacotePorUsuarioAdmin, self).changelist_view(request, extra_context=extra_context)

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
	    
    # list_display = ('nome', 'descricao', 'data_', 'data_implantacao')

admin.site.register(Token, TokenAdmin)