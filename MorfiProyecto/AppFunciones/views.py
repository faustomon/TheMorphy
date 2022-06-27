from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppFunciones.forms import *
from AppFunciones.models import *
# Create your views here.
def inicio(self):
    plantilla = loader.get_template("AppFunciones/templates/inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def restaurantes():
    plantilla = loader.get_template("AppFunciones/templates/inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)