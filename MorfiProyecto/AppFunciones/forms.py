from django import forms
from AppFunciones.models import *

class Resto_form(forms.ModelForm):
    class Meta:
        model = Restaurantes
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'provincia': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'horarios': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control', 'placeholder':"http://www.ejemplo.com"}),
            'imagen': forms.URLInput(attrs={'class':'form-control', 'placeholder':"Dirección web de imagen"}),
        }