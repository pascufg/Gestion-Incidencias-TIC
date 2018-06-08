from django.contrib import admin
from app.Gestion_Solicitudes.models import Solicitud, Actividad


# Register your models here.

class SolicitudesRegristado(admin.ModelAdmin):
    list_display = ["__unicode__", "CI", "estado","prioridad","alumno","equipo"]
    list_filter = ["registro","activo"]
    search_fields = ["CI","estado"]
    class Meta:
        model = Solicitud

class ActividadRegistrada(admin.ModelAdmin):
    list_display = ["__unicode__", "registro", "alumno","solicitud","resolucion","solucion"]
    list_filter = ["alumno","solicitud"]
    search_fields = ["alumno","solicitud"]
    class Meta:
        model = Actividad

admin.site.register(Solicitud, SolicitudesRegristado)
admin.site.register(Actividad, ActividadRegistrada)
