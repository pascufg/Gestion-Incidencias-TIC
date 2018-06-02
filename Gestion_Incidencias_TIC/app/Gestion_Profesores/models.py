from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from app.Gestion_Alumnos.models import Equipo
from app.Gestion_Centros.models import Centro, Curso


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True,)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    activo = models.BooleanField("Activo", default=True)
    centro = models.ForeignKey(Centro, null=True, blank=True, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='post_image', blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre

class ProfesorCurso(models.Model):
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    descripcion = models.TextField(max_length=30)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.curso.nombre
    def __unicode__(self):
        return self.curso.nombre
