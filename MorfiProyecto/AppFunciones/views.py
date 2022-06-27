from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy, reverse
from AppFunciones.forms import *
from AppFunciones.models import *
from django.views.generic import *
from django.views.generic.detail import *
from django.views.generic.edit import *

# Create your views here.

class RecetasList(ListView):
    model = Recetas
    template_name = "AppFunciones/templates/receta_list.html"

class RecetaDetail(DetailView):
    model = Recetas
    template_name = "AppFunciones/templates/receta_detalle.html"

class RecetaCreate(CreateView):
    model = Recetas
    template_name = "AppFunciones/templates/receta_form.html"
    form_class = RecetasFormulario
    def get_success_url(self):
        return reverse('DetalleRecetas', kwargs={'pk':self.object.pk})

class RecetaUpdate(UpdateView):
    model = Recetas
    template_name = "AppFunciones/templates/receta_form.html"
    form_class = RecetasFormulario
    def get_success_url(self):
        return reverse('DetalleRecetas', kwargs={'pk':self.object.pk})

class RecetaDelete(DeleteView):
    model = Recetas
    template_name = 'recetas_confirm_delete.html'
    def get_success_url(self):
        return reverse('ListaRecetas')
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
# Inicio
def inicio(request):
    return render(request, "inicio.html")

# Seccion Restaurantes
class restaurante(ListView):
    model = Restaurantes
    template_name = 'restaurante.html'

class restaurantes_crear(CreateView):
    model = Restaurantes
    template_name = 'restaurantes_crear.html'
    form_class = Resto_form
    def get_success_url(self):
        return reverse('restaurantes_detalle', kwargs={'pk':self.object.pk})

class restaurantes_detalle(DetailView):
    model = Restaurantes
    template_name = 'restaurantes_detalle.html'
