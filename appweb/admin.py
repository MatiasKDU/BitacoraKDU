from django.contrib import admin
from .models import Usuario, Computador, Activo, AccionCrud, Asignacion, CaractHardware, CaractSoftware, Dispositivo, EstadoActivo, Licencia, MantencionActivo, ProcesoServidor, TipoServidor, Servidor, Registroaccion, TipoUsuario, SistemaOperativo


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Computador)
admin.site.register(Activo)
admin.site.register(AccionCrud)
admin.site.register(Asignacion)
admin.site.register(CaractHardware)
admin.site.register(CaractSoftware)
admin.site.register(Dispositivo)
admin.site.register(EstadoActivo)
admin.site.register(Licencia)
admin.site.register(MantencionActivo)
admin.site.register(ProcesoServidor)
admin.site.register(TipoServidor)
admin.site.register(Servidor)
admin.site.register(Registroaccion)
admin.site.register(TipoUsuario)
admin.site.register(SistemaOperativo)
