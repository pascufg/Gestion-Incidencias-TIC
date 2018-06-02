from django.urls import reverse_lazy
from django.views.generic import ListView

from app.Gestion_Profesores.models import ProfesorCurso


class ListarCursoProfesor(ListView):
    model = ProfesorCurso
    template_name = 'cursoprofesor.html'
    slug_field = 'profesor_id'

    def get_queryset(self):
        queryset = super(ListarCursoProfesor, self).get_queryset()
        return queryset.filter(profesor_id=self.kwargs['profesor_id'])

class ListarCursoAsignaturaProfesor(ListView):
    model = ProfesorCurso
    template_name = 'curso_aula.html'
    slug_field = 'profesor_id'

    def get_queryset(self):
        queryset = super(ListarCursoAsignaturaProfesor, self).get_queryset()
        print(queryset)
        return queryset.filter(profesor_id=self.kwargs['profesor_id'])