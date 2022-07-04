from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = UsernameField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Modificar nombre de usuario', required=False)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repita su nueva contraseña', widget=forms.PasswordInput, required=False)
    nombre = forms.CharField(label='Modificar nombre', required=False)
    apellido = forms.CharField(label='Modificar apellido', required=False)
    edad = forms.IntegerField(label='Modificar edad', required=False)
    imagen = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nombre', 'apellido', 'edad']
        help_texts = {k:'' for k in fields}