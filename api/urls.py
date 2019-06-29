from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from usuarios_meviro.views import UsuarioEspacoViewSet
from administrativo.views import PacoteViewSet, ContratoViewSet, PeriodosReservaRecursoViewSet, RegraViewSet
from infra.views import RecursoViewSet
from logs.views import LogAcessoEspacoUsuarioViewSet, LogUsoFerramentaUsuarioViewSet
from api.views import api_login, authorize_bridge

router = routers.DefaultRouter()
router.register(r'u suarios_meviro', UsuarioEspacoViewSet)
router.register(r'log_acesso', LogAcessoEspacoUsuarioViewSet)
router.register(r'log_uso', LogUsoFerramentaUsuarioViewSet)
# router.register(r'api/assinatura', AssinaturaViewSet)

usuario_espaco_list = UsuarioEspacoViewSet.as_view({
    'get': 'list',
})
usuario_espaco_detail = UsuarioEspacoViewSet.as_view({
    'get': 'retrieve'
})
usuario_espaco_add = UsuarioEspacoViewSet.as_view({
	'post': 'create'
})
usuario_espaco_update = UsuarioEspacoViewSet.as_view({
	'post':'update'
})
####
pacotes_list = PacoteViewSet.as_view({
    'get': 'list',
})

pacotes_detail = PacoteViewSet.as_view({
    'get': 'retrieve'
})

pacotes_add = PacoteViewSet.as_view({
	'post': 'create'
})

pacotes_update = PacoteViewSet.as_view({
	'post':'update'
})

####
recursos_list = RecursoViewSet.as_view({
    'get': 'list',
})

recursos_detail = RecursoViewSet.as_view({
    'get': 'retrieve'
})

recursos_add = RecursoViewSet.as_view({
	'post': 'create'
})

recursos_update = RecursoViewSet.as_view({
	'post':'update'
})

####
log_acesso_list = LogAcessoEspacoUsuarioViewSet.as_view({
    'get': 'list',
})

log_acesso_detail = LogAcessoEspacoUsuarioViewSet.as_view({
    'get': 'retrieve'
})

log_acesso_add = LogAcessoEspacoUsuarioViewSet.as_view({
	'post': 'create'
})

log_acesso_update = LogAcessoEspacoUsuarioViewSet.as_view({
	'post':'update'
})
####
log_uso_list = LogUsoFerramentaUsuarioViewSet.as_view({
    'get': 'list',
})

log_uso_detail = LogUsoFerramentaUsuarioViewSet.as_view({
    'get': 'retrieve'
})

log_uso_add = LogUsoFerramentaUsuarioViewSet.as_view({
	'post': 'create'
})

log_uso_update = LogUsoFerramentaUsuarioViewSet.as_view({
	'post':'update'
})


urlpatterns = [
    path('', include(router.urls)),
 # BEGIN: API PATHS
   
    path('login', api_login), #cria e/ou retorna o token de autenticação a partir de usuario e senha (django superuser)
   	path('usuario_espaco/', usuario_espaco_list, name='usuario-espaco-list'),
    path('usuario_espaco/<int:pk>/', usuario_espaco_detail, name='usuario-espaco-detail'),
    path('usuario_espaco/add/', usuario_espaco_add, name='usuario-espaco-add'),
    path('usuario_espaco/<int:pk>/update/', usuario_espaco_update, name='usuario-espaco-update'),

    path('pacotes/', pacotes_list, name='pacotes-list'),
    path('pacotes/<int:pk>/', pacotes_detail, name='pacotes-detail'),
    path('pacotes/add/', pacotes_add, name='pacotes-add'),
    path('pacotes/<int:pk>/update/', pacotes_update, name='pacotes-update'),

    path('recursos/', recursos_list, name='recursos-list'),
    path('recursos/<int:pk>/', recursos_detail, name='recursos-detail'),
    path('recursos/add/', recursos_add, name='recursos-add'),
    path('recursos/<int:pk>/update/', recursos_update, name='recursos-update'),

    path('log_acesso/', log_acesso_list, name='log-acesso-list'),
    path('log_acesso/<int:pk>/', log_acesso_detail, name='log-acesso-detail'),
    path('log_acesso/add/', log_acesso_add, name='log-acesso-add'),
    path('log_acesso/<int:pk>/update/', log_acesso_update, name='log-acesso-update'),

    path('log_uso/', log_uso_list, name='log-uso-list'),
    # path('log_uso/detail/<int:pk>/', log_uso_detail, name='log-uso-detail'),
    path('log_uso/add/', log_uso_add, name='log-uso-add'),
    # path('log_uso/update/<int:pk>/update/', log_uso_update, name='log-uso-update')
    path('p/<int:id_arduino>/<int:id_usuario>', authorize_bridge)
    
  # END: API PATHS

]
