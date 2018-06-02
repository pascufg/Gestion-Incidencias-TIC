from django.contrib import admin

# Register your models here.
from app.Gestion_Profesores.models import Profesor, ProfesorCurso


class ProfesorRegristado(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellidos","dni","registro","activo", "foto", "user"]
    list_filter = ["registro","activo"]
    search_fields = ["nombre","dni"]
    class Meta:
        model = Profesor

class ProfesorCursoRegristado(admin.ModelAdmin):
    list_display = ["id", "curso", "profesor","registro","activo"]
    list_filter = ["id", "curso", "profesor","registro","activo"]
    search_fields = ["id", "curso", "profesor","registro","activo"]
    class Meta:
        model = ProfesorCurso

admin.site.register(Profesor, ProfesorRegristado)
admin.site.register(ProfesorCurso, ProfesorCursoRegristado)