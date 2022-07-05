from django.urls import path, include
from AppSesiones.views import *

urlpatterns = [
    path("", include("AppFunciones.urls")),
    path('login/', login_request, name = "login"),
    path('logout/', logout_request, name = "logout"),
    # path('registro/', registro, name = "registro"),
    path('registro/', registro.as_view(), name = 'registro'),
    path('editar_perfil/', editar_perfil, name = 'editar_perfil'),
    path('perfil/<int:pk>/', perfil.as_view(), name = "perfil"),
    path('perfil_eliminar/<int:pk>/', perfil_eliminar.as_view(), name='perfil_eliminar'),
    ]