from django.contrib import admin
from .models import LogAcessoEspacoUsuario, LogUsoFerramentaUsuario


admin.site.register(LogAcessoEspacoUsuario)
admin.site.register(LogUsoFerramentaUsuario)