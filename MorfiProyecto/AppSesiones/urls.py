from django.urls import path, include
from AppSesiones import views
from AppFunciones.views import *

urlpatterns = [
    path('login/', views.login_request, name = "login"),
    path('register/', views.register, name = "register"),
    path('AppFunciones/', include('AppFunciones.urls')),
    ]