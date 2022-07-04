from email.policy import default
from django.db import models
from django.urls import reverse

class Recetas(models.Model):
    nombre_de_receta = models.CharField(max_length=60)
    ingredientes = models.TextField(max_length=300)
    instrucciones = models.TextField(max_length=300)
    autor = models.CharField(max_length=60)
    imagen_de_comida = models.URLField(max_length=300, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('nombre_de_receta-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nombre_de_receta

class Restaurantes(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=600, blank=True, null=True)
    direccion = models.CharField(max_length=100)
    link_direccion = models.URLField(max_length=300, blank=True, null=True, default="https://www.google.com.ar/maps")
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    horarios = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    imagen = models.URLField(max_length=300, blank=True, null=True, default="https://previews.123rf.com/images/blotty/blotty1707/blotty170700012/82776756-vector-vintage-burger-drawing-mano-dibuja-la-ilustraci%C3%B3n-de-comida-r%C3%A1pida-monocromo-.jpg")
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    resto = models.ForeignKey(Restaurantes, null=True, default=1, related_name="comentarios", on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=50, blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(max_length=1000, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' % (self.resto.titulo, self.nombre)