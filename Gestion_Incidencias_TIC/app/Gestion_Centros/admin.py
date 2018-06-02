from django.contrib import admin
from app.Gestion_Centros.models import Centro, Aula, Curso, CursoAula, Asignatura, AsignaturaCurso, Tema
from .forms import RegCentroModelForm

# Register your models here.
class CentroRegristado(admin.ModelAdmin):
    list_display = ["__unicode__", "codigo", "nombre","localidad","registro","activo"]
    form = RegCentroModelForm
    list_filter = ["registro"]
    search_fields = ["nombre", "codigo"]
    #class Meta:
    #   model = Centro

class AulaRegistrada(admin.ModelAdmin):
    list_display = ["__unicode__", "codigo", "nombre","registro"]
    list_filter = ["registro"]
    search_fields = ["nombre", "codigo"]
    class Meta:
        model = Aula

class CursoRegistrado(admin.ModelAdmin):
    list_display = ["__unicode__", "codigo", "nombre","registro"]
    list_filter = ["registro"]
    search_fields = ["nombre", "codigo"]
    class Meta:
        model = Curso

class CursoAulaRegistrado(admin.ModelAdmin):

    list_display = ["__unicode__", "curso", "aula","registro","activo"]
    list_filter = ["registro"]
    search_fields = ["curso", "aula", "activo"]
    class Meta:
        model = CursoAula



class AsignaturaRegistrado(admin.ModelAdmin):

    list_display = ["__unicode__", "asignatura","registro","activo"]
    list_filter = ["registro"]
    search_fields = ["asignatura", "activo","alunno"]
    class Meta:
        model = Asignatura


class AsignaturaCursoRegistrado(admin.ModelAdmin):

    list_display = ["__unicode__", "asignatura","curso","registro","activo"]
    list_filter = ["registro"]
    search_fields = ["asignatura", "curso", "activo","alunno"]
    class Meta:
        model = AsignaturaCurso

class TemaRegistrado(admin.ModelAdmin):

    list_display = ["__unicode__", "nombre","fichero","asignatura","registro","activo"]
    list_filter = ["registro"]
    search_fields = ["nombre", "fichero", "asignatura"]
    class Meta:
        model = Tema


admin.site.register(Centro, CentroRegristado)
admin.site.register(Aula, AulaRegistrada)
admin.site.register(Curso, CursoRegistrado)
admin.site.register(CursoAula, CursoAulaRegistrado)
admin.site.register(Asignatura, AsignaturaRegistrado)
admin.site.register(AsignaturaCurso, AsignaturaCursoRegistrado)
admin.site.register(Tema,TemaRegistrado)