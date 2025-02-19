from django.shortcuts import render

from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework import viewsets

from .serializer import UsuarioSerializer, ComputadorSerializer, ActivoSerializer, AccionCrudSerializer, AsignacionSerializer, CaractHardwareSerializer, CaractSoftwareSerializer, DispositivoSerializer, EstadoActivoSerializer, LicenciaSerializer, MantencionActivoSerializer, ProcesoServidorSerializer, TipoServidorSerializer, ServidorSerializer, RegistroaccionSerializer, TipoUsuarioSerializer, SistemaOperativoSerializer

from .models import Usuario, Computador, Activo, AccionCrud, Asignacion, CaractHardware, CaractSoftware, Dispositivo, EstadoActivo, Licencia, MantencionActivo, ProcesoServidor, TipoServidor, Servidor, Registroaccion, TipoUsuario, SistemaOperativo


# Create your views here.

class UsuarioView(viewsets.ModelViewSet):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


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
    
    @action(detail=True, methods=['put'], url_path='modificar-computador')
    def modificar_computador(self, request, pk=None):
        computador = self.get_object()
        serializer = self.get_serializer(computador, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)
    
    @action(detail=True, methods=['delete'], url_path='eliminar-computador')
    def eliminar_computador(self, request, pk=None):
        computador = self.get_object()
        computador.delete()
        return Response({"Mensaje":"Computador eliminado correctamente!"}, status=204)


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
    
    @action(detail=True, methods=['put'], url_path= 'modificar-activo')
    def modificar_activo(self, request, pk=None):
        activo = self.get_object()
        serializer = self.get_serializer(activo, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)
        
    @action(detail=True, methods = ['delete'], url_path='eliminar-activo')
    def eliminar_activo(self, request, pk=None):
        activo = self.get_object()
        activo.delete()
        return Response({"Mensaje":"Activo eliminado correctamente!"}, status=204)

class AccionCrudView(viewsets.ModelViewSet):##sdasdasdasads
    serializer_class = AccionCrudSerializer
    queryset = AccionCrud.objects.all()

class AsignacionView(viewsets.ModelViewSet):
    serializer_class = AsignacionSerializer
    queryset = Asignacion.objects.all()

class CaractHardwareView(viewsets.ModelViewSet):
    serializer_class = CaractHardwareSerializer
    queryset = CaractHardware.objects.all()

class CaractSoftwareView(viewsets.ModelViewSet):
    serializer_class = CaractSoftwareSerializer
    queryset = CaractSoftware.objects.all()

class DispositivoView(viewsets.ModelViewSet):
    serializer_class = DispositivoSerializer
    queryset = Dispositivo.objects.all()

class EstadoActivoView(viewsets.ModelViewSet):
    serializer_class = EstadoActivoSerializer
    queryset = EstadoActivo.objects.all()

class LicenciaView(viewsets.ModelViewSet):
    serializer_class = LicenciaSerializer
    queryset = Licencia.objects.all()

class MantencionActivoView(viewsets.ModelViewSet):
    serializer_class = MantencionActivoSerializer
    queryset = MantencionActivo.objects.all()

class ProcesoServidorView(viewsets.ModelViewSet):
    serializer_class = ProcesoServidorSerializer
    queryset = ProcesoServidor.objects.all() 

class TipoServidorView(viewsets.ModelViewSet):
    serializer_class = TipoServidorSerializer
    queryset = TipoServidor.objects.all()

class ServidorView(viewsets.ModelViewSet):
    serializer_class = ServidorSerializer
    queryset = Servidor.objects.all()

class RegistroaccionView(viewsets.ModelViewSet):
    serializer_class = RegistroaccionSerializer
    queryset = Registroaccion.objects.all()

class TipoUsuarioView(viewsets.ModelViewSet):
    serializer_class = TipoUsuarioSerializer
    queryset = TipoUsuario.objects.all()

class SistemaOperativoView(viewsets.ModelViewSet):
    serializer_class = SistemaOperativoSerializer
    queryset = SistemaOperativo.objects.all()