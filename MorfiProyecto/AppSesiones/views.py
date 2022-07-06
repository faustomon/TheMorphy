from pyexpat import model
from statistics import mode
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from AppSesiones.forms import *
from AppFunciones.urls import *
from AppSesiones.models import *
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy

#---------------Login-----------------
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                context = {'mensaje': f'Bienvenido {usuario}!!'}
                return render(request, 'inicio.html', context=context)
            else:
                context = {'mensaje': f'Disculpe, el usuario o la contraseña son incorrectos o no existen!!'}
                return render(request, 'inicio.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()            
            context = {'error':errors,'form':form}
            return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,"login.html", {'form':form} )

#---------------Logout-----------------
def logout_request(request):
    logout(request)
    return redirect('Inicio')

#---------------Registro-----------------
class Perfil_crear(CreateView):
    model = Sesion_perfil
    template_name = "registro.html"
    form_class = Perfil_registro_form
    def post(self, request):
        modelo = Sesion_perfil()
        form = Perfil_registro_form(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password1']
            user = authenticate(username=usuario, password=contra)
            login(request, user)
            user.save()
            modelo.user = user
            modelo.nombre = usuario
            modelo.save()
            context = {'mensaje': f'Usuario creado correctamente. Bienvenido {usuario} :D !!'}
            return render(request,"inicio.html", context=context)
        else:
            context = {'mensaje': 'No se pudo crear el usuario'}
            return render(request,"inicio.html", context=context)

#---------------Editar-----------------
class Perfil_editar_views(UpdateView):
    model = Sesion_perfil
    template_name = "editar_perfil.html"
    form_class = Perfil_editar
    def get_success_url(self):
        return reverse('Inicio')