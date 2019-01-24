from django.contrib import admin
from .models import Secao, Armarios, IndiceAlerta, Riscos, Fornecedor, NotaFiscal, FuncaoFerramenta, Ferramenta

admin.site.register(Secao)
admin.site.register(Armarios)
admin.site.register(IndiceAlerta)
admin.site.register(Riscos)
admin.site.register(Fornecedor)
admin.site.register(NotaFiscal)
admin.site.register(FuncaoFerramenta)
admin.site.register(Ferramenta)
