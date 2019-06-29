from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    # path('', include(router.urls)),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('usuarios_espaco/', include('usuarios_meviro.urls')),
    path('infra/', include('infra.urls')),
    # path('administrativo/', include('administrativo.urls')),
    # path('financeiro/', include('financeiro.urls')),
   
]
