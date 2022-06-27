from django import forms
from AppFunciones.models import *

class RecetasFormulario(forms.ModelForm):
    class Meta:
        model = Recetas
        fields = '__all__'
        widgets = {
            'nombre_de_receta': forms.TextInput(attrs={'class':'form-control'}),
            'ingredientes': forms.TextInput(attrs={'class':'form-control'}),
            'instrucciones': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'imagen_de_comida': forms.URLInput(attrs={'class':'form-control', 'placeholder':"Dirección web de imagen"}),
        }
        # nombre_de_receta = models.CharField(max_length=60)
        # ingredientes = models.CharField(max_length=300)
        # instrucciones = models.CharField(max_length=300)
        # autor = models.CharField(max_length=60)
        # imagen_de_comida = models.URLField(max_length=300, blank=True, null=True)