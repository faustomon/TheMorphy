from django.urls import path
from AppFunciones import views
from AppFunciones.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("restaurante/", restaurante.as_view(), name="restaurante"),
    path("restaurantes_crear/", restaurantes_crear.as_view(), name="restaurantes_crear"),
    path("restaurantes_detalle/<int:pk>/", restaurantes_detalle.as_view(), name="restaurantes_detalle"),

]