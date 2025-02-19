from django.shortcuts import render

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

class ActivoView(viewsets.ModelViewSet):

    serializer_class = ActivoSerializer
    queryset = Activo.objects.all()

class AccionCrudView(viewsets.ModelViewSet):
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