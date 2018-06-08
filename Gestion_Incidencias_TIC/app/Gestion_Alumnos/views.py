# Create your views here.
from Tools.scripts.highlight import default_ansi
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from requests import request

from app.Gestion_Alumnos.forms import AlumnoForm, EquipoForm
from app.Gestion_Alumnos.models import Alumno, Equipo
from app.Gestion_Centros.models import Aula


class Perfil(DetailView):
    model = Alumno
    template_name='perfil.html'

class RegistarAlumno(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'registraralumno.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Alumno registrado correctamente')
        return reverse_lazy('alumno:registraralumno')


class RegistarEquipo(CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'registrarequipo.html'

    def get_initial(self):
        aula = self.kwargs['aula_id']
        # Get the initial dictionary from the superclass method
        initial = super(RegistarEquipo, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()

        initial['aula'] = aula
        return initial

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Equipo registrado correctamente')
        return reverse_lazy('centro:inicio')




class ListarAlumno(ListView):
    model = Alumno
    template_name = 'listaralumno.html'

    def get_success_url(self):
        return reverse_lazy('centro:inicio')

class ListarCursoAlumno(ListView):
    model = Alumno
    template_name = 'cursoalumno.html'
    slug_field = 'profesor_id'

    def get_queryset(self):
        queryset = super(ListarCursoAlumno, self).get_queryset()
        print(queryset)
        return queryset.filter(curso_id=self.kwargs['curso_id'])

class ListarEquipoAula(ListView):
    model = Equipo
    template_name = 'aula_equipo.html'
    slug_field = 'aula_id'

    def get_queryset(self):
        queryset = super(ListarEquipoAula, self).get_queryset()
        print(queryset)
        return queryset.filter(aula_id=self.kwargs['aula_id'])


class EliminarEquipo(DeleteView):
    model = Equipo
    def get_success_url(self):
        #messages.add_message(self.request, messages.SUCCESS, 'Equipo eliminado correctamente')
        return reverse_lazy('centro:inicio')

class EditarEquipo(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'registrarequipo.html'

    def get_success_url(self):
        return reverse_lazy('solicitud:listarsolicitud')