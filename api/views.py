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
from infra.models import ArduinoAuth, SecaoAssinatura
from usuarios_meviro.models import UsuarioEspaco
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

def authorize_arduino(request, id_arduino, id_usuario):
    try:
        arduino_secao = ArduinoAuth.objects.get(id_arduino=id_arduino)
    except:
        return JsonResponse({'auth': False});
    
    id_secao = arduino_secao.id_secao.id

    usuario = UsuarioEspaco.objects.get(id=id_usuario).values_list('id', 'tipo_assinatura_id')
    
    secao_assinaturas = SecaoAssinatura.objects.filter(id_assinatura=usuario.tipo_assinatura_id, id_secao=id_secao)

    
    if (not secao_assinaturas):
        return JsonResponse({'auth': False});
    
    return JsonResponse({'auth': True});
