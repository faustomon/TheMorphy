from django.urls import path, include
from AppSesiones.views import *

urlpatterns = [
    path("", include("AppFunciones.urls")),
    path('login/', login_request, name = "login"),
    path('logout/', logout_request, name = "logout"),
    path('registro/', Perfil_crear.as_view(), name = "registro"),
    path('editar_perfil/<pk>/', Perfil_editar_views.as_view(), name = 'editar_perfil'),
    ]