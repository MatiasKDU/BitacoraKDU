from django.db import models

class AccionCrud(models.Model):
    tipo_accion = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.tipo_accion or "AccionCrud"


class Activo(models.Model):
    tipo_activo = models.CharField(max_length=45, blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    fecha_compromiso = models.DateField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    computador = models.ForeignKey('Computador', on_delete=models.CASCADE, blank=True, null=True)
    servidor = models.ForeignKey('Servidor', on_delete=models.CASCADE, blank=True, null=True)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE, blank=True, null=True)
    estado_activo = models.ForeignKey('EstadoActivo', on_delete=models.CASCADE, blank=True, null=True)
    licencia = models.ForeignKey('Licencia', on_delete=models.CASCADE, blank=True, null=True)
    mantencion_activo = models.ForeignKey('MantencionActivo', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Activo: {self.tipo_activo} - Ingreso: {self.fecha_ingreso}"


class Asignacion(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Asignacion: {self.usuario} -> {self.activo}"


class CaractHardware(models.Model):
    bateria = models.CharField(max_length=45, blank=True, null=True)
    ram = models.CharField(max_length=45, blank=True, null=True)
    ram_hz = models.IntegerField(blank=True, null=True)
    grafica = models.CharField(max_length=45, blank=True, null=True)
    tipo_procesador = models.CharField(max_length=45, blank=True, null=True)
    modelo_procesador = models.CharField(max_length=45, blank=True, null=True)
    tipo_almacenamiento = models.CharField(max_length=45, blank=True, null=True)
    espacio_almacenamiento = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Hardware: {self.tipo_procesador} {self.modelo_procesador}"


class CaractSoftware(models.Model):
    numero_anydesk = models.IntegerField(blank=True, null=True)
    sistema_operativo = models.ForeignKey('SistemaOperativo', on_delete=models.CASCADE)

    def __str__(self):
        return f"Software: AnyDesk {self.numero_anydesk}"


class Computador(models.Model):
    nombre_equipo = models.CharField(max_length=40, blank=True, null=True)
    numero_factura = models.IntegerField(blank=True, null=True)
    marca = models.CharField(max_length=45, blank=True, null=True)
    modelo = models.CharField(max_length=45, blank=True, null=True)
    serie = models.CharField(max_length=50)
    numero_modelo = models.CharField(max_length=45, blank=True, null=True)
    disponibilidad = models.SmallIntegerField(blank=True, null=True)
    estado_computador = models.IntegerField()
    caract_hardware = models.ForeignKey(CaractHardware, on_delete=models.CASCADE)
    caract_software = models.ForeignKey(CaractSoftware, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_equipo or self.serie


class Dispositivo(models.Model):
    nombre_dispositivo = models.CharField(max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    serie = models.CharField(max_length=100, blank=True, null=True)
    disponibilidad = models.CharField(max_length=45, blank=True, null=True)
    almacenamiento = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.nombre_dispositivo or self.serie or "Dispositivo"


class EstadoActivo(models.Model):
    descripcion_estadoactivo = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.descripcion_estadoactivo or "EstadoActivo"


class Licencia(models.Model):
    tipo_licencia = models.CharField(max_length=45, blank=True, null=True)
    descripcion_licencia = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.tipo_licencia or "Licencia"


class MantencionActivo(models.Model):
    detalle_mantencion = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)  # Renombrado de 'fecha_' a 'fecha'
    responsable = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f"Mantencion: {self.detalle_mantencion}"


class ProcesoServidor(models.Model):
    nombre_proceso = models.CharField(max_length=50, blank=True, null=True)
    numero_procesos = models.IntegerField(blank=True, null=True)
    identificacion = models.CharField(max_length=50, blank=True, null=True)
    ruta = models.CharField(max_length=50, blank=True, null=True)
    archivo = models.CharField(max_length=50, blank=True, null=True)
    levantamiento = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre_proceso or "ProcesoServidor"


class Registroaccion(models.Model):
    detalles = models.CharField(max_length=255, blank=True, null=True)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    accion_crud = models.ForeignKey(AccionCrud, on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registro: {self.detalles}"


class Servidor(models.Model):
    nombre_servidor = models.CharField(max_length=45, blank=True, null=True)
    tipo_servidor = models.ForeignKey('TipoServidor', on_delete=models.CASCADE)
    id_instancia = models.CharField(max_length=255, blank=True, null=True)
    estado_instancia = models.CharField(max_length=45, blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)
    nombre_cuenta = models.CharField(max_length=45, blank=True, null=True)
    ssh = models.SmallIntegerField(blank=True, null=True)
    estado_usuario = models.CharField(max_length=45, blank=True, null=True)
    llave = models.SmallIntegerField(blank=True, null=True)
    estado_llave = models.CharField(max_length=45, blank=True, null=True)
    servicios_aplicaciones = models.CharField(max_length=255, blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    proceso_servidor = models.ForeignKey(ProcesoServidor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_servidor or "Servidor"


class SistemaOperativo(models.Model):
    nombre_sistemaoperativo = models.CharField(max_length=45, blank=True, null=True)
    versionso = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.nombre_sistemaoperativo or "SistemaOperativo"


class TipoServidor(models.Model):
    descripcion_tiposervidor = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.descripcion_tiposervidor or "TipoServidor"


class TipoUsuario(models.Model):
    descripcion_usuario = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.descripcion_usuario or "TipoUsuario"


class Usuario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)
    correo_tbk = models.CharField(max_length=255, blank=True, null=True)
    llave_ssh = models.CharField(max_length=255, blank=True, null=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre or "Usuario"
