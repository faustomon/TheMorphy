from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from AppSesiones.forms import *
from AppFunciones.urls import *
from AppSesiones.models import *
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy


# Create your views here.

def logout_request(request):
    logout(request)
    return redirect('Inicio')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
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

class registro(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registro.html'
    success_url: reverse_lazy('login')

# def registro(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             form.save()
#             return render(request,"inicio.html")
#     else:
#         form = UserRegisterForm()
#     return render(request,"registro.html" ,  {"form":form})

class perfil(DetailView):
    model = Sesion_perfil
    template_name = 'perfil.html'

class perfil_eliminar(DeleteView):
    model = Sesion_perfil
    template_name = 'perfil_eliminar.html'
    def get_success_url(self):
        return reverse('Inicio')

def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.nombre = informacion['nombre']
            usuario.apellido = informacion['apellido']
            usuario.edad = informacion['edad']
            usuario.imagen = informacion['imagen']
            form.save()
            return render(request, 'inicio.html', {'mensaje': 'Datos cambiados exitosamente'})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, 'editar_perfil.html', {'form':form, 'usuario':usuario.username})