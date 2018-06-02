from django.db import models
from app.Gestion_Centros.models import Centro, Aula, Curso
from django.contrib.auth.admin import User

class Equipo(models.Model):
    codigo = models.CharField(max_length=15)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=120)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    activo = models.BooleanField("Activo", default=True)
    aula = models.ForeignKey(Aula, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo

    def __unicode__(self):
        return self.codigo

class Alumno(models.Model):
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
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre
