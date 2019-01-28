from django.contrib import admin
from .models import Secao, SecaoAssinatura, Armarios, FuncaoFerramenta, Ferramenta, Arduino, ArduinoAuth

admin.site.register(Secao)
admin.site.register(SecaoAssinatura)
admin.site.register(Armarios)
admin.site.register(FuncaoFerramenta)
admin.site.register(Ferramenta)
admin.site.register(Arduino)
admin.site.register(ArduinoAuth)
