# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import UsuarioEspaco


class UsuarioEspacoAdmin(admin.ModelAdmin):
    list_display = ('primeiro_nome', 'sobrenome', 'email', 'tipo_assinatura')
    # list_filter = ('tipo_assinatura','tipo_funcionario')

    change_list_template = "admin/usuario_espaco/change_list.html"

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Lista de todos os usuários do espaço'}
        return super(UsuarioEspacoAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.site_header = "Espaço MeViro"
admin.site.site_title = "Gestão do Espaço MeViro"
admin.site.index_title = "Bem vindo ao sistema de controle do Espaço MeViro."

admin.site.register(UsuarioEspaco, UsuarioEspacoAdmin)
# admin.site.register(Avatar)
