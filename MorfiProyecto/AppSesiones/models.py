from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sesion_perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="sesion_perfil")
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to='perfiles', blank=True, null=True)

    def __str__(self):
        return self.nombre