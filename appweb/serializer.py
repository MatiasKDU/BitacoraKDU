from rest_framework import serializers

from .models import Usuario, Computador, Activo, AccionCrud, Asignacion, CaractHardware, CaractSoftware, Dispositivo, EstadoActivo, Licencia, MantencionActivo, ProcesoServidor, TipoServidor, Servidor, Registroaccion, TipoUsuario, SistemaOperativo


class UsuarioSerializer(serializers.ModelSerializer): # 19-feb
    class Meta:
        model = Usuario
        fields = '__all__'       



class  ComputadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computador
        fields = '__all__'
    
class ActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activo
        fields = '__all__'
    
class AccionCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccionCrud
        fields = '__all__'

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = '__all__'
    
class CaractHardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaractHardware
        fields = '__all__'

class CaractSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaractSoftware
        fields = '__all__'

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class EstadoActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoActivo
        fields = '__all__'

class LicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licencia
        fields = '__all__'

class MantencionActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MantencionActivo
        fields = '__all__'

class ProcesoServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcesoServidor
        fields = '__all__'


class TipoServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServidor
        fields = '__all__'


class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = '__all__'

class RegistroaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registroaccion
        fields = '__all__'

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class SistemaOperativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistemaOperativo
        fields = '__all__'