from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("AppFunciones.urls")),
    path("", include("AppSesiones.urls")),
]
handler404 = "MorfiProyecto.views.error_404"