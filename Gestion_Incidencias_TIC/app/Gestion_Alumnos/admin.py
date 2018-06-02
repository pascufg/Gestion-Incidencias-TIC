from django.contrib import admin

from app.Gestion_Alumnos.models import Alumno, Equipo
# Register your models here.

class AlumnoRegristado(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellidos","dni","registro","activo", "foto", "user"]
    list_filter = ["registro","activo"]
    search_fields = ["nombre","dni"]
    class Meta:
        model = Alumno

class EquipoRegristado(admin.ModelAdmin):
    list_display = ["codigo","modelo","marca","aula"]
    list_filter = ["registro","activo","aula"]
    search_fields = ["codigo","marca","aula"]
    class Meta:
        model = Equipo

admin.site.register(Alumno, AlumnoRegristado)
admin.site.register(Equipo, EquipoRegristado)