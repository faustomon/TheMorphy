from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from AppFunciones.forms import *
from AppFunciones.models import *
from django.views.generic import *
from django.views.generic.detail import *
from django.views.generic.edit import *

# Create your views here.
#---------------Recetas-----------------
class RecetasList(ListView):
    model = Recetas
    template_name = "AppFunciones/templates/receta_list.html"

class RecetaDetail(DetailView):
    model = Recetas
    template_name = "AppFunciones/templates/receta_detalle.html"

class RecetaCreate(CreateView):
    model = Recetas
    template_name = "AppFunciones/templates/receta_form.html"
    form_class = RecetasFormulario
    def get_success_url(self):
        return reverse('DetalleRecetas', kwargs={'pk':self.object.pk})

class RecetaUpdate(UpdateView):
    model = Recetas
    template_name = "AppFunciones/templates/receta_form.html"
    form_class = RecetasFormulario
    def get_success_url(self):
        return reverse('DetalleRecetas', kwargs={'pk':self.object.pk})

class RecetaDelete(DeleteView):
    model = Recetas
    template_name = 'recetas_confirm_delete.html'
    def get_success_url(self):
        return reverse('ListaRecetas')

def buscar_receta(request):
    recetas = Recetas.objects.filter(nombre_de_receta__icontains = request.GET['search'])
    if recetas.exists():
        context = {'recetas':recetas}
    else:
        context = {'errors':'No se encontraron resultados, prueba de nuevo...'}
    return render(request,'receta_busqueda.html', context=context)

# Create your views here.
# Inicio
def inicio(request):
    return render(request, "inicio.html")

def acerca_de(request):
    return render(request, "acerca_de.html")

#---------------Restaurantes-----------------
class restaurante(ListView):
    model = Restaurantes
    template_name = 'restaurante.html'

class restaurantes_crear(CreateView):
    model = Restaurantes
    template_name = 'restaurantes_crear.html'
    form_class = Resto_form
    def get_success_url(self):
        return reverse('restaurantes_detalle', kwargs={'pk':self.object.pk})

class restaurantes_detalle(DetailView):
    model = Restaurantes
    template_name = 'restaurantes_detalle.html'

class restaurantes_eliminar(DeleteView):
    model = Restaurantes
    template_name = 'restaurantes_eliminar.html'
    def get_success_url(self):
        return reverse('restaurante')

class restaurantes_editar(UpdateView):
    model = Restaurantes
    template_name = 'restaurantes_editar.html'
    form_class = Resto_form
    def get_success_url(self):
        return reverse('restaurantes_detalle', kwargs={'pk':self.object.pk})

def restaurantes_buscar(request):
    restaurante = Restaurantes.objects.filter(nombre__icontains = request.GET['search'])
    if restaurante.exists():
        context = {'restaurante':restaurante}
    else:
        context = {'errors':'No se encontraron resultados, prueba de nuevo...'}
    return render(request,'restaurantes_buscar.html', context=context)


#---------------Comentarios-----------------
class comentario(ListView):
    model = Comentario
    template_name = 'comentario.html'

class comentarios_crear(CreateView):
    model = Comentario
    template_name = 'comentarios_crear.html'
    form_class = Comentario_form
    def form_valid(self, form):
        form.instance.resto_id = self.kwargs['pk']
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('comentarios_detalle', kwargs={'pk':self.object.pk})

class comentarios_detalle(DetailView):
    model = Comentario
    template_name = 'comentarios_detalle.html'

class comentarios_eliminar(DeleteView):
    model = Comentario
    template_name = 'comentarios_eliminar.html'
    def get_success_url(self):
        return reverse('comentario')

class comentarios_editar(UpdateView):
    model = Comentario
    template_name = 'comentarios_editar.html'
    form_class = Comentario_form
    def get_success_url(self):
        return reverse('comentarios_detalle', kwargs={'pk':self.object.pk})

def comentarios_buscar(request):
    comentario = Comentario.objects.filter(titulo__icontains = request.GET['search'])
    if comentario.exists():
        context = {'comentario':comentario}
    else:
        context = {'errors':'No se encontraron resultados, prueba de nuevo...'}
    return render(request,'comentarios_buscar.html', context=context)