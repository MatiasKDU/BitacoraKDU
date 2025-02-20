from django.shortcuts import render
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from .serializer import UsuarioSerializer, ComputadorSerializer, ActivoSerializer, AccionCrudSerializer, AsignacionSerializer, CaractHardwareSerializer, CaractSoftwareSerializer, DispositivoSerializer, EstadoActivoSerializer, LicenciaSerializer, MantencionActivoSerializer, ProcesoServidorSerializer, TipoServidorSerializer, ServidorSerializer, RegistroaccionSerializer, TipoUsuarioSerializer, SistemaOperativoSerializer, UserSerializer
from .models import Usuario, Computador, Activo, AccionCrud, Asignacion, CaractHardware, CaractSoftware, Dispositivo, EstadoActivo, Licencia, MantencionActivo, ProcesoServidor, TipoServidor, Servidor, Registroaccion, TipoUsuario, SistemaOperativo
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#---------------------------------Inicio Funcion del Login (20-02-2025)----------------------------------------------------------------------------

@api_view(['POST'])
def login(request):
    print(request.data) #datos que yo le envio

    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"error":"Contraseña incorrecta!"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):

    print(request.user)
    return Response("Estas logueado como {}".format(request.user.username), status=status.HTTP_200_OK)


#---------------------------------Fin Funcion del Login (20-02-2025)----------------------------------------------------------------------------



#----------------------------------Inicio Funciones del CRUD Clases (20-02-2025)-------------------------------------------------------------------
class UsuarioView(viewsets.ModelViewSet):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-usuario') #cuando requiere pk es True
    def obtener_usuario(self, request, pk=None): 
        usuarios = self.get_object()
        serializer = self.get_serializer(usuarios)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='listar-usuarios') #cuando no requiere pk es False
    def listar_usuario(self, request):
        usuarios = Usuario.objects.all()
        serializer = self.get_serializer(usuarios, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], url_path='crear-usuarios')
    def crear_usuarios(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-usuario')
    def modificar_usuarios(self, request, pk=None):
        usuario = self.get_object()  # Obtengo el usuario con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(usuario)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(usuario, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-usuario')
    def eliminar_usuario(self, request, pk=None):
        usuario = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(usuario)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            usuario.delete()
            return Response({"mensaje": "Usuario eliminado correctamente!"}, status=204)



class ComputadorView(viewsets.ModelViewSet):

    serializer_class = ComputadorSerializer
    queryset = Computador.objects.all()

    #Funciones para sobrenombrar al momento de obtener un compu con el metodo Get por medio de la Api -- 19 de feb
    @action(detail=True, methods=['get'], url_path='obtener-computador') #cuando requiere pk es True
    def obtener_computador(self, request, pk=None): 
        computador = self.get_object()
        serializer = self.get_serializer(computador)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='listar-computadores') #cuando no requiere pk es False
    def listar_computadores(self, request):
        computadores = Computador.objects.all()
        serializer = self.get_serializer(computadores, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], url_path='crear-computador')
    def crear_computadores(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-computador')
    def modificar_computador(self, request, pk=None):
        computador = self.get_object()  # Obtengo el usuario con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(computador)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(computador, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-computador')
    def eliminar_computador(self, request, pk=None):
        computador = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(computador)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            computador.delete()
            return Response({"mensaje": "Computador eliminado correctamente!"}, status=204)


class ActivoView(viewsets.ModelViewSet):

    serializer_class = ActivoSerializer
    queryset = Activo.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-activo')
    def obtener_activo(self, request, pk=None):
        activo = self.get_object()
        serializer = self.get_serializer(activo)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-activos')
    def listar_activos(self, request):
        activo = Activo.objects.all()
        serializer = self.get_serializer(activo, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-activo')
    def crear_activo(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-activo')
    def modificar_activo(self, request, pk=None):
        activo = self.get_object()  # Obtengo el usuario con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(activo)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(activo, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-activo')
    def eliminar_activo(self, request, pk=None):
        activo = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(activo)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            activo.delete()
            return Response({"mensaje": "Activo eliminado correctamente!"}, status=204)

class AccionCrudView(viewsets.ModelViewSet):
    serializer_class = AccionCrudSerializer
    queryset = AccionCrud.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-accioncrud')
    def obtener_accioncrud(self, request, pk=None):
        accioncrud = self.get_object()
        serializer = self.get_serializer(accioncrud)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-accioncrud')
    def listar_accioncrud(self, request):
        accioncrud = AccionCrud.objects.all()
        serializer = self.get_serializer(accioncrud, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-accioncrud')
    def crear_accioncrud(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-accioncrud')
    def modificar_accioncrud(self, request, pk=None):
        accioncrud = self.get_object()  # Obtengo el usuario con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(accioncrud)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(accioncrud, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-accioncrud')
    def eliminar_accioncrud(self, request, pk=None):
        accioncrud = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(accioncrud)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            accioncrud.delete()
            return Response({"mensaje": "Accion Crud eliminada correctamente!"}, status=204)

    

class AsignacionView(viewsets.ModelViewSet):
    serializer_class = AsignacionSerializer
    queryset = Asignacion.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-asignacion')
    def obtener_asignacion(self, request, pk=None):
        asignacion = self.get_object()
        serializer = self.get_serializer(asignacion)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-asignacion')
    def listar_asignacion(self, request):
        asignacion = Asignacion.objects.all()
        serializer = self.get_serializer(asignacion, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-asignacion')
    def crear_asignacion(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-asignacion')
    def modificar_asignacion(self, request, pk=None):
        asignacion = self.get_object()  # Obtengo el usuario con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(asignacion)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(asignacion, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-asignacion')
    def eliminar_asignacion(self, request, pk=None):
        asignacion = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(asignacion)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            asignacion.delete()
            return Response({"mensaje": "Asignacion eliminada correctamente!"}, status=204)

class CaractHardwareView(viewsets.ModelViewSet):
    serializer_class = CaractHardwareSerializer
    queryset = CaractHardware.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-caracthardware')
    def obtener_caracthardware(self, request, pk=None):
        caracthardware = self.get_object()
        serializer = self.get_serializer(caracthardware)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-caracthardware')
    def listar_caracthardware(self, request):
        caracthardware = CaractHardware.objects.all()
        serializer = self.get_serializer(caracthardware, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-caracthardware')
    def crear_caracthardware(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-caracthardware')
    def modificar_caracthardware(self, request, pk=None):
        caracthardware = self.get_object()  # Obtengo el usuario con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(caracthardware)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(caracthardware, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-caracthardware')
    def eliminar_caracthardware(self, request, pk=None):
        caracthardware = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(caracthardware)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            caracthardware.delete()
            return Response({"mensaje": "Caracteristicas de Hardware eliminadas correctamente!"}, status=204)


class CaractSoftwareView(viewsets.ModelViewSet):
    serializer_class = CaractSoftwareSerializer
    queryset = CaractSoftware.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-caractsoftware')
    def obtener_caractsoftware(self, request, pk=None):
        caractsoftware = self.get_object()
        serializer = self.get_serializer(caractsoftware)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-caractsoftware')
    def listar_caractsoftware(self, request):
        caractsoftware = CaractSoftware.objects.all()
        serializer = self.get_serializer(caractsoftware, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-caractsoftware')
    def crear_caractsoftware(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-caractsoftware')
    def modificar_caractsoftware(self, request, pk=None):
        caractsoftware = self.get_object()  # Obtengo el usuario con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(caractsoftware)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(caractsoftware, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-caractsoftware')
    def eliminar_caractsoftware(self, request, pk=None):
        caractsoftware = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(caractsoftware)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            caractsoftware.delete()
            return Response({"mensaje": "Caracteristicas de Hardware eliminadas correctamente!"}, status=204)

class DispositivoView(viewsets.ModelViewSet):
    serializer_class = DispositivoSerializer
    queryset = Dispositivo.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-dispositivo')
    def obtener_dispositivo(self, request, pk=None):
        dispositivo = self.get_object()
        serializer = self.get_serializer(dispositivo)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-dispositivo')
    def listar_dispositivo(self, request):
        dispositivo = Dispositivo.objects.all()
        serializer = self.get_serializer(dispositivo, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-dispositivo')
    def crear_dispositivo(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-dispositivo')
    def modificar_dispositivo(self, request, pk=None):
        dispositivo = self.get_object()  # Obtengo el dispositivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(dispositivo)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(dispositivo, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-dispositivo')
    def eliminar_dispositivo(self, request, pk=None):
        dispositivo = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(dispositivo)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            dispositivo.delete()
            return Response({"mensaje": "Dispositivo eliminado correctamente!"}, status=204)

class EstadoActivoView(viewsets.ModelViewSet):
    serializer_class = EstadoActivoSerializer
    queryset = EstadoActivo.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-estadoactivo')
    def obtener_estadoactivo(self, request, pk=None):
        estadoactivo = self.get_object()
        serializer = self.get_serializer(estadoactivo)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-estadoactivo')
    def listar_estadoactivo(self, request):
        estadoactivo = EstadoActivo.objects.all()
        serializer = self.get_serializer(estadoactivo, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-estadoactivo')
    def crear_estadoactivo(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-estadoactivo')
    def modificar_estadoactivo(self, request, pk=None):
        estadoactivo = self.get_object()  # Obtengo el estadoactivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(estadoactivo)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(estadoactivo, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-estadoactivo')
    def eliminar_estadoactivo(self, request, pk=None):
        estadoactivo = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(estadoactivo)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            estadoactivo.delete()
            return Response({"mensaje": "Estado de Activo eliminado correctamente!"}, status=204)

class LicenciaView(viewsets.ModelViewSet):
    serializer_class = LicenciaSerializer
    queryset = Licencia.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-licencia')
    def obtener_licencia(self, request, pk=None):
        licencia = self.get_object()
        serializer = self.get_serializer(licencia)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-licencia')
    def listar_licencia(self, request):
        licencia = Licencia.objects.all()
        serializer = self.get_serializer(licencia, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-licencia')
    def crear_licencia(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-licencia')
    def modificar_licencia(self, request, pk=None):
        licencia = self.get_object()  # Obtengo el estadoactivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(licencia)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(licencia, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-licencia')
    def eliminar_licencia(self, request, pk=None):
        licencia = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(licencia)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            licencia.delete()
            return Response({"mensaje": "Licencia eliminada correctamente!"}, status=204)

class MantencionActivoView(viewsets.ModelViewSet):
    serializer_class = MantencionActivoSerializer
    queryset = MantencionActivo.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-mantencionactivo')
    def obtener_mantencionactivo(self, request, pk=None):
        mantencionactivo = self.get_object()
        serializer = self.get_serializer(mantencionactivo)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-mantencionactivo')
    def listar_mantencionactivo(self, request):
        mantencionactivo = MantencionActivo.objects.all()
        serializer = self.get_serializer(mantencionactivo, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-mantencionactivo')
    def crear_mantencionactivo(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-mantencionactivo')
    def modificar_mantencionactivo(self, request, pk=None):
        mantencionactivo = self.get_object()  # Obtengo el estadoactivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(mantencionactivo)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(mantencionactivo, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-mantencionactivo')
    def eliminar_mantencionactivo(self, request, pk=None):
        mantencionactivo = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(mantencionactivo)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            mantencionactivo.delete()
            return Response({"mensaje": "Licencia eliminada correctamente!"}, status=204)

class ProcesoServidorView(viewsets.ModelViewSet):
    serializer_class = ProcesoServidorSerializer
    queryset = ProcesoServidor.objects.all() 

    @action(detail=True, methods=['get'], url_path='obtener-procesoservidor')
    def obtener_procesoservidor(self, request, pk=None):
        procesoservidor = self.get_object()
        serializer = self.get_serializer(procesoservidor)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-procesoservidor')
    def listar_procesoservidor(self, request):
        procesoservidor = ProcesoServidor.objects.all()
        serializer = self.get_serializer(procesoservidor, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-procesoservidor')
    def crear_procesoservidor(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-procesoservidor')
    def modificar_procesoservidor(self, request, pk=None):
        procesoservidor = self.get_object()  # Obtengo el estadoactivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(procesoservidor)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(procesoservidor, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-procesoservidor')
    def eliminar_procesoservidor(self, request, pk=None):
        procesoservidor = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(procesoservidor)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            procesoservidor.delete()
            return Response({"mensaje": "Proceso de Servidor eliminado correctamente!"}, status=204)

class TipoServidorView(viewsets.ModelViewSet):
    serializer_class = TipoServidorSerializer
    queryset = TipoServidor.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-tiposervidor')
    def obtener_tiposervidor(self, request, pk=None):
        tiposervidor = self.get_object()
        serializer = self.get_serializer(tiposervidor)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-tiposervidor')
    def listar_tiposervidor(self, request):
        tiposervidor = TipoServidor.objects.all()
        serializer = self.get_serializer(tiposervidor, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-tiposervidor')
    def crear_tiposervidor(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-tiposervidor')
    def modificar_tiposervidor(self, request, pk=None):
        tiposervidor = self.get_object()  # Obtengo el estadoactivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(tiposervidor)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(tiposervidor, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-tiposervidor')
    def eliminar_tiposervidor(self, request, pk=None):
        tiposervidor = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(tiposervidor)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            tiposervidor.delete()
            return Response({"mensaje": "Proceso de Servidor eliminado correctamente!"}, status=204)

class ServidorView(viewsets.ModelViewSet):
    serializer_class = ServidorSerializer
    queryset = Servidor.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-servidor')
    def obtener_servidor(self, request, pk=None):
        servidor = self.get_object()
        serializer = self.get_serializer(servidor)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-servidor')
    def listar_servidor(self, request):
        servidor = Servidor.objects.all()
        serializer = self.get_serializer(servidor, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-servidor')
    def crear_servidor(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-servidor')
    def modificar_servidor(self, request, pk=None):
        servidor = self.get_object()  # Obtengo el estadoactivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(servidor)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(servidor, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-servidor')
    def eliminar_servidor(self, request, pk=None):
        servidor = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(servidor)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            servidor.delete()
            return Response({"mensaje": "Servidor eliminado correctamente!"}, status=204)

class RegistroaccionView(viewsets.ModelViewSet):
    serializer_class = RegistroaccionSerializer
    queryset = Registroaccion.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-registroaccion')
    def obtener_registroaccion(self, request, pk=None):
        registroaccion = self.get_object()
        serializer = self.get_serializer(registroaccion)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-registroaccion')
    def listar_registroaccion(self, request):
        registroaccion = Registroaccion.objects.all()
        serializer = self.get_serializer(registroaccion, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-registroaccion')
    def crear_registroaccion(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-registroaccion')
    def modificar_registroaccion(self, request, pk=None):
        registroaccion = self.get_object()  # Obtengo el estadoactivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(registroaccion)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(registroaccion, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-registroaccion')
    def eliminar_registroaccion(self, request, pk=None):
        registroaccion = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(registroaccion)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            registroaccion.delete()
            return Response({"mensaje": "Registro de Accion eliminada correctamente!"}, status=204)

class TipoUsuarioView(viewsets.ModelViewSet):
    serializer_class = TipoUsuarioSerializer
    queryset = TipoUsuario.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-tipousuario')
    def obtener_tipousuario(self, request, pk=None):
        tipousuario = self.get_object()
        serializer = self.get_serializer(tipousuario)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-tipousuario')
    def listar_tipousuario(self, request):
        tipousuario = TipoUsuario.objects.all()
        serializer = self.get_serializer(tipousuario, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-tipousuario')
    def crear_tipousuario(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-tipousuario')
    def modificar_tipousuario(self, request, pk=None):
        tipousuario = self.get_object()  # Obtengo el estadoactivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(tipousuario)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(tipousuario, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-tipousuario')
    def eliminar_tipousuario(self, request, pk=None):
        tipousuario = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(tipousuario)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            tipousuario.delete()
            return Response({"mensaje": "Registro de Accion eliminada correctamente!"}, status=204)

class SistemaOperativoView(viewsets.ModelViewSet):
    serializer_class = SistemaOperativoSerializer
    queryset = SistemaOperativo.objects.all()

    @action(detail=True, methods=['get'], url_path='obtener-sistemaoperativo')
    def obtener_sistemaoperativo(self, request, pk=None):
        sistemaoperativo = self.get_object()
        serializer = self.get_serializer(sistemaoperativo)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='listar-sistemaoperativo')
    def listar_sistemaoperativo(self, request):
        sistemaoperativo = SistemaOperativo.objects.all()
        serializer = self.get_serializer(sistemaoperativo, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods= ['post'], url_path='crear-sistemaoperativo')
    def crear_sistemaoperativo(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status= 400)
    
    @action(detail=True, methods=['get', 'put'], url_path='modificar-sistemaoperativo')
    def modificar_sistemaoperativo(self, request, pk=None):
        sistemaoperativo = self.get_object()  # Obtengo el estadoactivo con el ID PK

        if request.method == 'GET': 
            serializer = self.get_serializer(sistemaoperativo)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(sistemaoperativo, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=True, methods=['get', 'delete'], url_path='eliminar-sistemaoperativo')
    def eliminar_sistemaoperativo(self, request, pk=None):
        sistemaoperativo = self.get_object() 

        if request.method == 'GET':  
            serializer = self.get_serializer(sistemaoperativo)
            return Response(serializer.data)

        elif request.method == 'DELETE': 
            sistemaoperativo.delete()
            return Response({"mensaje": "Registro de Accion eliminada correctamente!"}, status=204)
        
#-----------------------------------Fin Funciones del CRUD Clases (20-02-2025)----------------------------------------------------------------------