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
from django.core import files
from django.conf import settings
from django.core.files import File
from django.http import HttpResponse

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
   
    brigde_recurso = None
    try:
        brigde_recurso = Bridge.objects.get(recurso_id=id_arduino)
    except:
        return JsonResponse({'auth': False});
    
    id_recurso = brigde_recurso.recurso_id

    usuario = UsuarioEspaco.objects.get(id=id_usuario)

    pacotesPorUsuario = PacotePorUsuario.objects.filter(usuario=usuario.id)

    autorizado = False;

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
                    autorizado = True;
                    break;

    if (not autorizado):
        return JsonResponse({'auth': False});
    
    # bridge = Bridge.objects.get(id=brigde_recurso.id)
    log_uso_ferramenta = LogUsoFerramentaUsuario(id_usuario=usuario, id_bridge=brigde_recurso)
    log_uso_ferramenta.save()
    
    return JsonResponse({'auth': True});



def file_upload(request):
    save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
    path = default_storage.save(save_path, request.FILES['file'])
    return default_storage.path(path)

def get_bridge_authorization_id_usuarios(request, id_arduino):
   
    brigde_recurso = Bridge.objects.get(recurso_id=id_arduino)
    id_recurso = brigde_recurso.recurso_id

    usuarios = UsuarioEspaco.objects.values_list('id', flat=True)
    usuarios_autorizados_por_bridge = "["
    usuario = None
    for usuario in usuarios:
        autorizado = False
        
        pacotesPorUsuario = PacotePorUsuario.objects.filter(usuario=usuario)
        for pacotePorUsuario in pacotesPorUsuario:
            pacote = pacotePorUsuario.pacote
            pacoteObject = Pacote.objects.get(id=pacote.id)
            regras = pacoteObject.regra.all()
            for regra in regras:
                regraObject = Regra.objects.get(id=regra.id)
                recursos = regraObject.recurso.all()
                for recurso in recursos:
                    recursoObject = Recurso.objects.get(id=recurso.id)
                    if recursoObject.id == id_recurso:
                        autorizado = True;
                        usuarios_autorizados_por_bridge = usuarios_autorizados_por_bridge + str(usuario) + ';' 
                        break
                if autorizado:
                    break
            if autorizado:
                break
    
    usuarios_autorizados_por_bridge = usuarios_autorizados_por_bridge + "]"

    file_path = 'info_files' + '/info.txt'
    with open(file_path, 'w') as text_file:
        myfile = File(text_file)
        myfile.write(usuarios_autorizados_por_bridge)
    
    filename = "info.txt"
    content = usuarios_autorizados_por_bridge
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response

    
    
