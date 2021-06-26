from django import forms
from django.forms import ModelForm
from .models import Receta, Tipo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TipoForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    resumen = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Tipo
        fields = ('nombre', 'resumen',)


class RecetaForm(ModelForm):

    titulo = forms.CharField(label='Titulo',max_length=200, widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        ))
    
    imagen = forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))

    ingredientes = forms.CharField(label='Ingredientes', max_length=5000,help_text= 'Separe los ingredientes con comas', widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))

    tipo = forms.ModelChoiceField(queryset=Tipo.objects.all(), label='Tipo',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))
    
    descripcion = forms.CharField(label='Descripcion', max_length=5000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))


    class Meta:
        model = Receta
        fields = ('titulo','imagen','ingredientes','tipo','descripcion')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
