from django.contrib import admin

# Register your models here.
from . models import Tipo, Receta, Negocio, TipoNego, Perfil, Comuna

admin.site.register(Tipo)
admin.site.register(Receta)
admin.site.register(Negocio)
admin.site.register(TipoNego)
admin.site.register(Perfil)
admin.site.register(Comuna)