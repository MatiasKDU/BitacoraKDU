from django.urls import path, include

from rest_framework import routers

from appweb import views

router = routers.DefaultRouter()

router.register(r'usuarios', views.UsuarioView, 'usuarios')
router.register(r'computadores', views.ComputadorView, 'computadores')
router.register(r'activos', views.ActivoView, 'activos')
router.register(r'accioncrud', views.AccionCrudView, 'accioncrud')
router.register(r'asignacion', views.AsignacionView, 'asignacion')
router.register(r'caracthardware', views.CaractHardwareView, 'caracthardware')
router.register(r'caractsoftware', views.CaractSoftwareView, 'caractsoftware')
router.register(r'dispositivo', views.DispositivoView, 'dispositivo')
router.register(r'estadoactivo', views.EstadoActivoView, 'estadoactivo')
router.register(r'licencia', views.LicenciaView, 'licencia')
router.register(r'mantencionactivo', views.MantencionActivoView, 'mantencionactivo')
router.register(r'procesoservidor', views.ProcesoServidorView, 'procesoservidor')
router.register(r'tiposervidor', views.TipoServidorView, 'tiposervidor')
router.register(r'servidores', views.ServidorView, 'servidores')
router.register(r'registroaccion', views.RegistroaccionView, 'registroaccion')
router.register(r'tipousuario', views.TipoUsuarioView, 'tipousuario')
router.register(r'sistemaoperativo', views.SistemaOperativoView, 'sistemaoperativo')


urlpatterns = [

    path("api/v1/", include(router.urls))
]