from django import forms
from django.db.models import Model

from app.Gestion_Alumnos.models import Alumno, Equipo


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
            'foto',
            'nombre',
            'apellidos',
            'dni',
            'email',
            'centro',
            'curso'

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'dni': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'email': forms.EmailInput(attrs={'class': 'form-control required=True'}),
            'centro': forms.Select(attrs={'class': 'form-control required=True'}),
            'curso': forms.Select(attrs={'class': 'form-control required=True'}),
        }
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'codigo',
            'marca',
            'modelo',
            'aula',
            'descripcion',

        ]

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'marca': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'aula': forms.Select(attrs={'readonly':'false','class': 'form-control required=True',}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control required=True'}),

        }