from django.db import models
from django.urls import reverse

class Recetas(models.Model):
    nombre_de_receta = models.CharField(max_length=60)
    ingredientes = models.CharField(max_length=300)
    instrucciones = models.CharField(max_length=300)
    autor = models.CharField(max_length=60)
    imagen_de_comida = models.URLField(max_length=300, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('nombre_de_receta-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nombre_de_receta