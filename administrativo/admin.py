from django.contrib import admin
from .models import Assinatura, IntervalosHorarios, DiasSemana, Fornecedor

class TipoAssinaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'periodo')
    
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Lista dos tipos de assinatura'}
        return super(TipoAssinaturaAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(Assinatura, TipoAssinaturaAdmin)
admin.site.register(IntervalosHorarios)
admin.site.register(DiasSemana)
admin.site.register(Fornecedor)
