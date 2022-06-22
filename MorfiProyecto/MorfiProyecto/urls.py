from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("TheMorphy", include("AppFunciones.urls")),
    path("Sesiones", include("AppSesiones.urls")),
]
