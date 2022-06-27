from django.urls import path
from AppFunciones import views
from AppFunciones.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("restaurantes/", restaurantes.as_view(), name="restaurantes"),

]