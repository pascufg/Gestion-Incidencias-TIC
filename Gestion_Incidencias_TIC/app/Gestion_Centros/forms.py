from django import forms

from app.Gestion_Centros.models import Centro, Asignatura, Aula, Tema, CursoAula


class RegCentroModelForm(forms.ModelForm):
    class Meta:
        model = Centro
        fields = ["codigo","nombre","localidad","cp","provincia","incidencia","activo"]

    def clean_nombre(self):
        print(self.cleaned_data)
        _nombre = self.cleaned_data.get("nombre")
        #Validaciones
        return _nombre

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control required=True'}))
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'class': 'form-control required=True'}))
    asunto = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control required=True'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control required=True'}))

class RegAulaModelForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ["codigo","nombre","numero_puestos","centro"]

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'numero_puestos': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'centro': forms.Select(attrs={'class': 'form-control required=True'}),
        }

class RegTemaModelForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ["nombre","nombreFichero","fichero","curso","asignatura"]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'nombreFichero': forms.TextInput(attrs={'class': 'form-control required=True'}),
            'curso': forms.Select(attrs={'readonly':'false','class': 'form-control required=True'}),
            'asignatura': forms.Select(attrs={'readonly':'false','class': 'form-control required=True'}),
        }

class RegCursoAulaModelForm(forms.ModelForm):
    class Meta:
        model = CursoAula
        fields = ["curso","aula"]

        widgets = {
            'curso': forms.Select(attrs={'readonly':'false','class': 'form-control required=True'}),
            'aula': forms.Select(attrs={'class': 'form-control required=True'}),
        }
