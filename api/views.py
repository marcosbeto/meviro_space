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
from infra.models import Bridge, Recurso #, SecaoAssinatura
from usuarios_meviro.models import UsuarioEspaco, PacotePorUsuario
from administrativo.models import Pacote, Regra
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
   
    print("  tamaqui")
    brigde_recurso = None
    try:
        brigde_recurso = Bridge.objects.get(recurso_id=id_arduino)
    except:
        return JsonResponse({'auth': False});
    
    id_recurso = brigde_recurso.recurso_id

    usuario = UsuarioEspaco.objects.get(id=id_usuario)

    pacotesPorUsuario = PacotePorUsuario.objects.filter(usuario=usuario.id)

    autorizado = False;

    print(pacotesPorUsuario)

    for pacotePorUsuario in pacotesPorUsuario:
        pacote = pacotePorUsuario.pacote
        print(pacote)
        pacoteObject = Pacote.objects.get(id=pacote.id)
        regras = pacoteObject.regra.all()
        for regra in regras:
            regraObject = Regra.objects.get(id=regra.id)
            recursos = regraObject.recurso.all()
            for recurso in recursos:
                recursoObject = Recurso.objects.get(id=recurso.id)
                if recursoObject.id == id_recurso:
                    print("autorizado")
                    autorizado = True;
                    break;


    
    # secao_assinaturas = SecaoAssinatura.objects.filter(id_assinatura=usuario.tipo_assinatura_id, id_secao=id_secao)


    if (not autorizado):
        return JsonResponse({'auth': False});
    
    # bridge = Bridge.objects.get(id=brigde_recurso.id)
    log_uso_ferramenta = LogUsoFerramentaUsuario(id_usuario=usuario, id_bridge=brigde_recurso)
    log_uso_ferramenta.save()
    print('chegamo aqui')
    return Response({'auth': True},
                    status=HTTP_200_OK) #JsonResponse({'auth': True});
