from django.contrib import admin
from .models import Pacote, Contrato, PeriodosReservaRecurso, Regra

# class TipoAssinaturaAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'periodo')
    
#     def changelist_view(self, request, extra_context=None):
#         extra_context = {'title': 'Lista dos tipos de assinatura'}
#         return super(TipoAssinaturaAdmin, self).changelist_view(request, extra_context=extra_context)


class PacoteAdmin(admin.ModelAdmin):
	search_fields = ['nome']
	filter_horizontal = ('regra', 'contrato', 'curso','outraAtividade')
    # list_display = ('nome', 'descricao', 'data_', 'data_implantacao')

class RegraAdmin(admin.ModelAdmin):
    filter_horizontal = ('recurso', 'periodosReservaRecurso')

admin.site.register(Pacote, PacoteAdmin)
admin.site.register(Contrato)
admin.site.register(PeriodosReservaRecurso)
admin.site.register(Regra, RegraAdmin)
