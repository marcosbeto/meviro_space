from django.contrib import admin
from .models import Fornecedor, Recurso, Bridge, Area


class InfraAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {
            "Recursos": 2,
            "Bridges": 1,
            "BridgesAuth": 3,
            "Fornecedores": 4
        }
        app_dict = self._build_app_dict(request)
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list

class RecursoAdmin(admin.ModelAdmin):
	search_fields = ['nome']


class BridgeAdmin(admin.ModelAdmin):
	autocomplete_fields = ('recurso', )

# class BridgeAuthAdmin(admin.ModelAdmin):

# 	autocomplete_fields = ('id_recurso', 'id_bridge')
# admin_site = InfraAdminSite(name='infra')

admin.site.register(Fornecedor)
admin.site.register(Area)
admin.site.register(Recurso, RecursoAdmin)
admin.site.register(Bridge, BridgeAdmin)
# admin.site.register(BridgeAuth, BridgeAuthAdmin)


