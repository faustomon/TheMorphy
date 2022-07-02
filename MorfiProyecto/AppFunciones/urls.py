from django.urls import path
from AppFunciones import views
from AppFunciones.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    #---------------Recetas-----------------
    path("recetas_lista/", RecetasList.as_view(), name="ListaRecetas"),
    path("recetas/<pk>/", RecetaDetail.as_view(), name="DetalleRecetas"),
    path("recetas/", RecetaCreate.as_view(), name="CrearRecetas"),
    path("recetas/edicion/<pk>/", RecetaUpdate.as_view(), name="EditarRecetas"),
    path("recetas/eliminar/<pk>/", RecetaDelete.as_view(), name="EliminarRecetas"),
    #---------------Restaurantes-------------
    path("restaurante/", restaurante.as_view(), name="restaurante"),
    path("restaurantes_crear/", restaurantes_crear.as_view(), name="restaurantes_crear"),
    path("restaurantes_detalle/<int:pk>/", restaurantes_detalle.as_view(), name="restaurantes_detalle"),
    #---------------Criticas-------------
    path("critica/", critica.as_view(), name="critica"),
    path("criticas_crear/", criticas_crear.as_view(), name="criticas_crear"),
    path("criticas_detalle/<int:pk>/", criticas_detalle.as_view(), name="criticas_detalle"),

]