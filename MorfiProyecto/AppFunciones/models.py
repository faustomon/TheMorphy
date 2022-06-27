from django.db import models

# Create your models here.
class Restaurantes(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    horarios = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True, null=True)
    imagen = models.URLField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.nombre