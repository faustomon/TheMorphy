from django.urls import path
from AppFunciones import views
from AppFunciones.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("restorauntes/", restos, name="restos"),
    path("recetas/", recetas, name="recetas"),

]