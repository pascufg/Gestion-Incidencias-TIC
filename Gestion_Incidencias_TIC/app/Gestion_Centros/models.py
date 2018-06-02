from django.db import models

# Create your models here.

class Centro(models.Model):
    codigo = models.IntegerField()
    nombre  = models.CharField(max_length=60)
    localidad = models.CharField(max_length=50)
    cp = models.IntegerField()
    provincia = models.CharField(max_length=40)
    incidencia = models.TextField(max_length=120, null=True, blank=True)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

class Aula(models.Model):
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    numero_puestos = models.IntegerField()
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    centro = models.ForeignKey(Centro, null=True, blank=True, on_delete=models.CASCADE)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    letra = models.CharField(max_length=30, blank=True)
    codigo = models.CharField(max_length=30)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

class CursoAula(models.Model):
    curso =  models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    aula  =  models.ForeignKey(Aula, null=True, blank=True, on_delete=models.CASCADE)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.curso.nombre

    def __unicode__(self):
        return self.curso.nombre

class Asignatura(models.Model):
    asignatura = models.CharField(max_length=50)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    descripcion = models.TextField(max_length=30)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.asignatura

    def __unicode__(self):
        return self.asignatura

class AsignaturaCurso(models.Model):

    asignatura = models.ForeignKey(Asignatura, null=True, blank=True, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    icono = models.ImageField(upload_to='post_image', blank=True)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.curso.nombre

    def __unicode__(self):
        return self.curso.nombre

class Tema(models.Model):
    nombre =  models.CharField(max_length=50)
    nombreFichero = models.CharField(max_length=50)
    fichero = models.FileField(upload_to='tema')
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, null=True, blank=True, on_delete=models.CASCADE)
    registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre