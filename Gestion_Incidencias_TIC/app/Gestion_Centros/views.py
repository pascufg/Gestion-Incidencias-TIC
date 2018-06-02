import pkg_resources
from cms.middleware import user
from django.conf import settings
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.db.models.sql.compiler import cursor_iter
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from psycopg2._psycopg import cursor

from app.Gestion_Centros.models import AsignaturaCurso, Tema, Asignatura, Aula, CursoAula, Centro
from .forms import ContactForm, RegAulaModelForm, RegTemaModelForm, RegCursoAulaModelForm
from ..Gestion_Alumnos.models import Alumno
# Create your views here.

def login(request):
    titulo = "Bienvenido"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" %(request.user)
    context = {
        "titulo_login": titulo,
    }
    return render(request, "../templates", context)

def contacto(request):
    form = ContactForm(request.POST or None)

    #alumno = Alumno.objects.get(user=request.user)
    if form.is_valid():
        form_nombre = form.cleaned_data.get("nombre")
        form_email = form.cleaned_data.get("email")
        form_asunto = form.cleaned_data.get("asunto")
        form_mensaje = form.cleaned_data.get("mensaje")
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from]
        email_mensaje = "%s: %s enviado por %s " %(form_nombre, form_mensaje, form_email)
        send_mail(form_asunto,
                  email_mensaje,
                  email_from,
                  email_to,
                  fail_silently=False
                  )
    context = {
        "contact": form,
    }
    return render(request, "contact.html", context)

def privacidad(request):
    return render(request, "privacidad.html")

def inicio(request):
    titulo = "Bienvenido"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" % (request.user)
        
        print(request.user.id)
        curso = AsignaturaCurso.objects.all()
    context = {
        "titulo_login": titulo,
        "curso":curso
    }
    return render(request, "home.html", context)


class AsignaturasList(ListView):
    model = AsignaturaCurso
    template_name = 'asignatura.html'
    slug_field = 'curso_id'

    def get_queryset(self):
        queryset = super(AsignaturasList, self).get_queryset()
        print(queryset)
        return queryset.filter(curso_id=self.kwargs['curso_id'])

class AsignaturasProfesorList(ListView):
    model = AsignaturaCurso
    template_name = 'curso_profesor.html'
    slug_field = 'curso_id'

    def get_queryset(self):
        queryset = super(AsignaturasProfesorList, self).get_queryset()
        print(queryset)
        return queryset.filter(curso_id=self.kwargs['curso_id'])



class Temas(ListView):
    model = Tema
    template_name='tema.html'
    slug_field = 'asignatura_id'

    def get_queryset(self):
        queryset = super(Temas, self).get_queryset()
        print(queryset)
        return queryset.filter(asignatura_id=self.kwargs['asignatura_id']).filter(curso_id=self.kwargs['curso_id'])

class RegistrarTema(CreateView):
    form_class = RegTemaModelForm
    template_name = 'registrar_tema.html'

    def get_initial(self):
        curso = self.kwargs['curso_id']
        asignatura = self.kwargs['asignatura_id']
        # Get the initial dictionary from the superclass method
        initial = super(RegistrarTema, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()

        initial['curso'] = curso
        initial['asignatura'] = asignatura

        return initial

    def get_success_url(self):
        return reverse_lazy('centro:inicio')

class RegistrarAula(CreateView):
    form_class = RegAulaModelForm
    template_name = 'registrar_aula.html'

    def get_success_url(self):
        return reverse_lazy('centro:inicio')



class ListarAulaCurso(ListView):
    model = CursoAula
    template_name = 'aula_curso.html'
    slug_field = 'curso_id'

    def get_queryset(self):
        queryset = super(ListarAulaCurso, self).get_queryset()
        print(queryset)
        return queryset.filter(curso_id=self.kwargs['curso_id'])


class RegistrarCursoAula(CreateView):
    form_class = RegCursoAulaModelForm
    template_name = 'registrar_curso_aula.html'

    def get_initial(self):
        curso = self.kwargs['curso_id']
        print(curso)
        initial = super(RegistrarCursoAula, self).get_initial()
        initial = initial.copy()
        initial['curso'] = curso
        return initial

    def get_success_url(self):
        return reverse_lazy('centro:inicio')
