from django.contrib.auth.models import User
from django.db import models
from app.Gestion_Alumnos.models import Alumno, Equipo
# Create your models here.

Tipo = (
    ('Sotfware', 'Sotfware'),
    ('Hardware', 'Hardware'),
)
Estado = (
    ('Abierta', 'Abierta'),
    ('Cerrada', 'Cerrada'),
    ('Retrasada', 'Retrasada'),
    ('Fijada', 'Fijada'),
)

Prioridad = (
    ('Normal', 'Normal'),
    ('Alta', 'Alta'),
    ('Muy alta', 'Muy alta'),
)
Tipo_Solicitud = (
    ('Incidencia', 'Incidencia'),
    ('Peticion', 'Peticion'),
    ('Problema', 'Problema'),
)

class Solicitud(models.Model):
    CI = models.CharField(max_length=10, choices=Tipo)
    estado =   models.CharField(max_length=20, choices=Estado)
    prioridad  = models.CharField(max_length=30, choices=Prioridad)
    tipo = models.CharField(max_length=20, choices=Tipo_Solicitud)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, null=True, blank=True, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=250)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return "{}, {}".format(type(self).__name__, self.id, self.CI)


    def __unicode__(self):
        return "{}, {}".format(type(self).__name__, self.id, self.CI)

class Actividad(models.Model):
    registro = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(Solicitud, null=True, blank=True, on_delete=models.CASCADE)
    resolucion = models.DateTimeField(null=True, blank=True)
    solucion = models.TextField(max_length=250, null=True, blank=True)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.solicitud.CI


    def __unicode__(self):
        return self.solicitud.CI




