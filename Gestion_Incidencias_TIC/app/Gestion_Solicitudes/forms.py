from django import forms

from app.Gestion_Solicitudes.models import Solicitud


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