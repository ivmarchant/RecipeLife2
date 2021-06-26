from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

#PROVEEDORES
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='example.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

class TipoNego(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		ordering = ['nombre']
	def __str__(self):
		return self.nombre

class Comuna(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		ordering = ['nombre']
	def __str__(self):
		return self.nombre

class Negocio(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField(max_length=1000)
    descripcion = models.TextField(max_length=1000)
    web = models.TextField(max_length=1000)
    imagen = models.ImageField(null=True, blank=True, default='descarga.png')
    tipo = models.ForeignKey('TipoNego', on_delete=models.SET_NULL, null=True, blank=False)
    comuna = models.ForeignKey('Comuna', on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """Returns the url to access a detail record for this manga."""
        return reverse('negocio_detail', args=[str(self.id)])


#FIN PROVEDORES

class Tipo(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		ordering = ['nombre']

	def __str__(self):
		return self.nombre


class Receta(models.Model):

    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(null=True, blank=True)
    ingredientes = models.TextField(max_length=300)
    tipo = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True, blank=False)
    descripcion = models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        """Returns the url to access a detail record for this manga."""
        return reverse('receta_detail', args=[str(self.id)])
