from django import forms
from django.shortcuts import render, redirect
from . models import Producto, Negocio
from . forms import NegocioForm, ProductoForm, UserRegisterForm
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect

from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages
from django.contrib.auth.models import User

from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )

def producto(request):
    num_producto=Producto.objects.all()

    return render(
        request,
        'producto.html',
        context={'num_producto':num_producto},
    )

def admin(request):
    return render(
        request,
        'admin.html',
    )


def recetas(request):
    return render(
        request,
        'recetas.html',
    )

def negocios(request):
    num_negocios=Negocio.objects.all()

    return render(
        request,
        'vista_proveedores.html',
        context={'num_negocios':num_negocios},
    )


class NegocioDetailView(generic.DetailView):
    model = Negocio


#Preguntas

def preguntas(request):
    return render(
        request,
        'preguntas.html',
    )

def contacto(request):
    if request.method=="POST":
        subject=request.POST['asunto']
        message="Remitente: " + request.POST['email'] + " Nombre: " + request.POST['nombre'] + ' Mensaje: ' + request.POST['msg']
        email_from=settings.EMAIL_HOST_USER
        recipent_list=['huntersupplier2@gmail.com']
        send_mail(subject,message,email_from,recipent_list)
        messages.success(request, f'Correo enviado')
    return render(request, "contacto.html")


def registro_usuarios(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect("registro_usuarios")
    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request, 'registro_usuarios.html', context)



# ================= CRUD Usuarios =================#

def listado_usuarios(request):
    user = User.objects.all()
    data = {
        'user':user
    }
    return render(
        request,
        'listado_usuarios.html',data
    )


def modificar_usuario(request, id):
    user= User.objects.get(id=id)
    data = {
        'form':UserRegisterForm(instance=user)
    }

    if request.method == 'POST':
        formulario = UserRegisterForm(data=request.POST, instance=user)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Usuario modificado')
            data['form'] = formulario
    return render (
        request,
        'modificar_usuario.html',data
    )



def eliminar_usuario(request, id):
    user =User.objects.get(id=id)
    user.delete()
    messages.success(request, f'Usuario eliminado')
    return redirect(to="listado_usuarios")



# ================= CRUD Recetas =================#

def listado_producto(request):
    producto= Producto.objects.all()
    data = {
        'producto':producto
    }
    return render(
        request,
        'listado_producto.html',data
    )


def crear_producto(request):
    data = {
        'form' :ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Producto creada')
            return redirect(to="index")
    return render(
        request,
        'nuevo_producto.html', data
    )


def modificar_producto(request, id):
    producto= Producto.objects.get(id=id)
    data = {
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Producto modificada exitosamente')
            data['form'] = ProductoForm(instance=Producto.objects.get(id=id))
    return render (
        request,
        'modificar_producto.html',data
    )


def eliminar_producto(request, id):
    producto =Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, f'Producto eliminada')
    return redirect(to="listado_producto") 

#PROVEDOORES

def crear_negocios(request):
    data = {
        'form' :NegocioForm()
    }

    if request.method == 'POST':
        formulario = NegocioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Negocio creado')
            return redirect(to="index")
    return render(
        request,
        'crear_proveedor.html', data
    )