from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django.contrib.auth.models import User

class Perfil_registro_form(UserCreationForm):
    username = UsernameField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}

class Perfil_editar(UserChangeForm):
    nombre = forms.CharField(label='Modificar nombre', required=False)
    apellido = forms.CharField(label='Modificar apellido', required=False)
    edad = forms.IntegerField(label='Modificar edad', required=False)
    imagen = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'edad', 'imagen']
        help_texts = {k:'' for k in fields}