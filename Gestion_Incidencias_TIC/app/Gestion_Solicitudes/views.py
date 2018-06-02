from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView
from django.views.generic.edit import UpdateView

from app.Gestion_Solicitudes.forms import SolicitudForm
from app.Gestion_Solicitudes.models import Solicitud
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


