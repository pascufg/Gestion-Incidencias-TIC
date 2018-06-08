import datetime
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import SelectDateWidget, extras

from app.Gestion_Solicitudes.models import Solicitud, Actividad


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'CI',
            'estado',
            'prioridad',
            'tipo',
            'alumno',
            'equipo',
            'descripcion',
        ]
        widgets = {
            'CI': forms.Select(attrs={'class': 'form-control required=True'}),
            'estado': forms.Select(attrs={'class': 'form-control required=True'}),
            'prioridad': forms.Select(attrs={'class': 'form-control required=True'}),
            'tipo': forms.Select(attrs={'class': 'form-control required=True'}),
            'alumno': forms.TextInput(attrs={'readonly':'true','class': 'form-control required=False'}),
            'equipo': forms.TextInput(attrs={'readonly':'true','class': 'form-control required=False'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control required=True'}),
        }

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = [
            'resolucion',
            'solucion',
            'activo',
        ]

        widgets = {
            'resolucion' : forms.DateInput(format='%d/%m/%Y'),
            'solucion': forms.TextInput(attrs={'class': 'form-control required=True'}),

        }