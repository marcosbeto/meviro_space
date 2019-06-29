from django.contrib import admin
from .models import OrdemDeServico, VendaPacotesPorUsuario, VendaCreditos


class VendaPacotesPorUsuarioAdmin(admin.ModelAdmin):
	filter_horizontal = ('pacotes', 'contratos')
	autocomplete_fields = ['usuario_meviro']


admin.site.register(OrdemDeServico)
admin.site.register(VendaPacotesPorUsuario, VendaPacotesPorUsuarioAdmin)
admin.site.register(VendaCreditos)