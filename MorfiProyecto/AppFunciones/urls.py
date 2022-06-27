from django.urls import path
from AppFunciones import views
from AppFunciones.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    #---------Recetas-----------------
    path("recetas_lista/", RecetasList.as_view(), name="ListaRecetas"),
    path("recetas/<pk>/", RecetaDetail.as_view(), name="DetalleRecetas"),
    path("recetas/", RecetaCreate.as_view(), name="CrearRecetas"),
    path("recetas/edicion/<pk>/", RecetaUpdate.as_view(), name="EditarRecetas"),
    path("recetas/eliminar/<pk>/", RecetaDelete.as_view(), name="EliminarRecetas"),

]