from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from AppSesiones.forms import UserRegisterForm
from AppFunciones.urls import *

# Create your views here.

def logout_request(request):
    logout(request)
    return redirect("inicio")
     

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request,"")
            else:
                return render(request,"")
        else:
            return render(request,"")
    form = AuthenticationForm()
    return render(request,"AppSesiones/templates/login.html", {'form':form} )



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppFunciones/templates/padre.html")
    else:
        form = UserRegisterForm()
    return render(request,"AppFunciones/padre.html" ,  {"form":form})