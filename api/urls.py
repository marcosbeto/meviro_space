from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from usuarios_espaco.views import PermissoesViewSet, AssinaturaViewSet, IntervalosHorariosViewSet, DiasSemanaViewSet, TipoFuncionarioViewSet, UsuarioEspacoViewSet
from ferramentas.views import FerramentaViewSet
from logs.views import LogAcessoEspacoUsuarioViewSet, LogUsoFerramentaUsuarioViewSet
from api.views import api_login

router = routers.DefaultRouter()
router.register(r'usuarios_espaco', UsuarioEspacoViewSet)
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
###
permissoes_list = PermissoesViewSet.as_view({
    'get': 'list',
})

permissoes_detail = PermissoesViewSet.as_view({
    'get': 'retrieve'
})

permissoes_add = PermissoesViewSet.as_view({
	'post': 'create'
})

permissoes_update = PermissoesViewSet.as_view({
	'post':'update'
})
####
assinatura_list = AssinaturaViewSet.as_view({
    'get': 'list',
})

assinatura_detail = AssinaturaViewSet.as_view({
    'get': 'retrieve'
})

assinatura_add = AssinaturaViewSet.as_view({
	'post': 'create'
})

assinatura_update = AssinaturaViewSet.as_view({
	'post':'update'
})

####
ferramenta_list = FerramentaViewSet.as_view({
    'get': 'list',
})

ferramenta_detail = FerramentaViewSet.as_view({
    'get': 'retrieve'
})

ferramenta_add = FerramentaViewSet.as_view({
	'post': 'create'
})

ferramenta_update = FerramentaViewSet.as_view({
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

    path('assinatura/', assinatura_list, name='assinatura-list'),
    path('assinatura/<int:pk>/', assinatura_detail, name='assinatura-detail'),
    path('assinatura/add/', assinatura_add, name='assinatura-add'),
    path('assinatura/<int:pk>/update/', assinatura_update, name='assinatura-update'),

    path('permissoes/', permissoes_list, name='permissoes-list'),
    path('permissoes/<int:pk>/', permissoes_detail, name='permissoes-detail'),
    path('permissoes/add/', permissoes_add, name='permissoes-add'),
    path('permissoes/<int:pk>/update/', permissoes_update, name='permissoes-update'),

    path('ferramenta/', ferramenta_list, name='ferramenta-list'),
    path('ferramenta/<int:pk>/', ferramenta_detail, name='ferramenta-detail'),
    path('ferramenta/add/', ferramenta_add, name='ferramenta-add'),
    path('ferramenta/<int:pk>/update/', ferramenta_update, name='ferramenta-update'),

    path('log_acesso/', log_acesso_list, name='log-acesso-list'),
    path('log_acesso/<int:pk>/', log_acesso_detail, name='log-acesso-detail'),
    path('log_acesso/add/', log_acesso_add, name='log-acesso-add'),
    path('log_acesso/<int:pk>/update/', log_acesso_update, name='log-acesso-update'),

    path('log_uso/', log_uso_list, name='log-uso-list'),
    # path('log_uso/detail/<int:pk>/', log_uso_detail, name='log-uso-detail'),
    path('log_uso/add/', log_uso_add, name='log-uso-add'),
    # path('log_uso/update/<int:pk>/update/', log_uso_update, name='log-uso-update')
    
  # END: API PATHS

]
