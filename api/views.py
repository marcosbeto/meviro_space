from django.shortcuts import render

#BEGIN: imports related to api authentication
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from infra.models import Bridge #, SecaoAssinatura
from usuarios_meviro.models import UsuarioEspaco
from logs.models import LogUsoFerramentaUsuario
#END: imports related to api authentication

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def api_login(request): #this method will return the token, if valid
    username = request.data.get("username")
    password = request.data.get("password")
        
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

def authorize_bridge(request, id_arduino, id_usuario):
    try:
        brigde_recurso = id_bridge#BridgeAuth.objects.get(id_bridge=id_bridge)
    except:
        return JsonResponse({'auth': False});
    
    id_recurso = bridge_recurso.id_recurso.id

    usuario = UsuarioEspaco.objects.get(id=id_usuario)
    
    secao_assinaturas = None#SecaoAssinatura.objects.filter(id_assinatura=usuario.tipo_assinatura_id, id_secao=id_secao)


    if (not secao_assinaturas):
        return JsonResponse({'auth': False});
    
    bridge = Bridge.objects.get(id=id_bridge)
    log_uso_ferramenta = LogUsoFerramentaUsuario(id_usuario=usuario, id_bridge=bridge)
    log_uso_ferramenta.save()

    return JsonResponse({'auth': True});
