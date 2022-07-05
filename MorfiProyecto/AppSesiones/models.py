from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sesion_perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sesion_perfil')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    imagen = models.ImageField(upload_to='perfiles', blank=True, null=True)
    #restaurantes
    #criticas
    #recetas
    #likes