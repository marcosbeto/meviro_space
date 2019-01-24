from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    # path('', include(router.urls)),
    
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('usuarios_espaco/', include('usuarios_espaco.urls')),
    path('ferramentas/', include('ferramentas.urls')),
   
]
