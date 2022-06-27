from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppFunciones.forms import *
from AppFunciones.models import *
from django.views.generic import ListView#, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
# Inicio
def inicio(request):
    return render(request, "inicio.html")

# Seccion Restaurantes
class restaurantes(ListView):
    model = Restaurantes
    template_name = 'restaurantes.html'