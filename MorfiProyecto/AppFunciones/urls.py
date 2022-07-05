from django.urls import path, include
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
    path("buscar/", buscar_receta, name="Buscar_Receta"),
    #---------------Restaurantes-------------
    path("restaurante/", restaurante.as_view(), name="restaurante"),
    path("restaurantes_crear/", restaurantes_crear.as_view(), name="restaurantes_crear"),
    path("restaurantes_detalle/<int:pk>/", restaurantes_detalle.as_view(), name="restaurantes_detalle"),
    path('restaurantes_eliminar/<int:pk>/', restaurantes_eliminar.as_view(), name='restaurantes_eliminar'),
    path('restaurantes_editar/<int:pk>/', restaurantes_editar.as_view(), name='restaurantes_editar'),
    path('restaurantes_buscar/', restaurantes_buscar, name='restaurantes_buscar'),
    #---------------Comentarios-------------
    path("comentario/", comentario.as_view(), name="comentario"),
    path("comentarios_crear/", comentarios_crear.as_view(), name="comentarios_crear"),
    path("comentarios_detalle/<int:pk>/", comentarios_detalle.as_view(), name="comentarios_detalle"),
    path('comentarios_eliminar/<int:pk>/', comentarios_eliminar.as_view(), name='comentarios_eliminar'),
    path('comentarios_editar/<int:pk>/', comentarios_editar.as_view(), name='comentarios_editar'),
    path('comentarios_buscar/', comentarios_buscar, name='comentarios_buscar'),

]
