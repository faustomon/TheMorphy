from django.urls import path, include
from AppSesiones import views
from AppFunciones.views import *

urlpatterns = [
    path("", include("AppFunciones.urls")),
    path('login/', views.login_request, name = "login"),
    path('logout/', views.logout_request, name = "logout"),
    path('registro/', views.registro, name = "registro"),
    path('editar_perfil/', views.editar_perfil, name = "editar_perfil"),
    ]