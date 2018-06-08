from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView

from app.Gestion_Solicitudes.forms import SolicitudForm, ActividadForm
from app.Gestion_Solicitudes.models import Solicitud, Actividad
from .models import Alumno

import json

class SolicitudCreate(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'registrarsolicitud.html'

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(SolicitudCreate, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()

        initial['alumno'] = self.request.user.alumno
        initial['equipo'] = self.request.user.alumno.equipo

        # etc...
        return initial

    def save(self, *args, **kwargs):  # redefinicion del metodo save() que contiene nuestro trigger
        # Aqui ponemos el codigo del trigger -------
        solicitud = Solicitud.objects.get(solicitud=self.solicitud)
        usuario = Solicitud.objects.get(usuario=self.usuario)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        actividad = Actividad.objects.create(solicitud=solicitud, usuario=usuario)
        actividad.save()
        return super(Actividad, self).save(*args, **kwargs)  # llamada al save() original con sus parámetros correspondientes

    def get_success_url(self):
        return reverse_lazy('centro:inicio')

def listarSolicitud(request):
    alumno = Alumno.objects.all().filter(user=request.user)
    solicitud = Solicitud.objects.all().filter(activo=True).filter(alumno=alumno)
    return render(request, template_name='listarsolicitud.html', context={'solicitud':solicitud})

def search(request):
    ci = request.GET.get('ci')
    solicitudes = Solicitud.objects.filter(CI=ci)
    solicitudes = [ search_serializer(solicitud) for solicitud in solicitudes ]
    return HttpResponse(json.dumps(solicitudes), content_type='application/json')

def search_serializer(solicitud):
    return {'id':solicitud.id, 'CI': solicitud.CI}


class EliminarSolicitud(DeleteView):
    model = Solicitud
    def get_success_url(self):
        return reverse_lazy('solicitud:listarsolicitud')

class EditarSolicitud(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'editarsolicitud.html'

    def get_success_url(self):
        return reverse_lazy('solicitud:listarsolicitud')

def ListarActividad(request):
    actividad = Actividad.objects.all().filter(activo=True)
    return render(request, template_name='mostraractividad.html', context={'actividad':actividad})

class DetalleSolicitud(DetailView):
    model = Solicitud
    template_name = 'detalle_solicitud.html'

    def get_queryset(self):
        queryset = super(DetalleSolicitud, self).get_queryset()
        print(queryset)
        return queryset.filter(pk=self.kwargs['pk'])

class DetalleSolicitud(DetailView):
    model = Solicitud
    template_name = 'detalle_solicitud.html'

    def get_queryset(self):
        queryset = super(DetalleSolicitud, self).get_queryset()
        print(queryset)
        return queryset.filter(pk=self.kwargs['pk'])

class CerrarSolicitud(UpdateView):
    model = Actividad
    form_class = ActividadForm
    template_name = 'cerrar_solicitud.html'

    def get_success_url(self):
        return reverse_lazy('centro:inicio')

