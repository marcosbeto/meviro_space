from django.contrib import admin
from .models import TreinamentoEmEquipamento, Curso, OutraAtividade


class OutraAtividadeAdmin(admin.ModelAdmin):
    filter_horizontal = ('treinamentoEmEquipamentos', )

class CursoAdmin(admin.ModelAdmin):
    filter_horizontal = ('treinamentoEmEquipamentos', )

class TreinamentoEmEquipamentoAdmin(admin.ModelAdmin):
    filter_horizontal = ('recurso', )

admin.site.register(TreinamentoEmEquipamento, TreinamentoEmEquipamentoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(OutraAtividade, OutraAtividadeAdmin)

