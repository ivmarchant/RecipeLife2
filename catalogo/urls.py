from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<str:username>', views.perfil, name='perfil'),
    path('vista_proovedor/', views.proveView, name='vista_proveedores'),
    path('contacto/' ,views.contacto, name='contacto'),
    path('recetas', views.recetas, name='recetas'),
    path('admin', views.admin, name='admin'),
    path('preguntas',views.preguntas, name='preguntas'),
    path('registro-usuario/', views.registro_usuarios, name='registro_usuarios'),
    path('listado-usuarios/', views.listado_usuarios, name='listado_usuarios'),
    path('modificar-usuario/<id>/', views.modificar_usuario, name='modificar_usuario'),
    path('eliminar-usuarios/<id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('listado-recetas/', views.listado_recetas, name='listado_recetas'),
    path('nueva-receta/', views.crear_recetas, name='nueva_receta'),
    path('modificar-recetas/<id>/', views.modificar_recetas, name='modificar_recetas'),
    path('eliminar-recetas/<id>/', views.eliminar_recetas, name='eliminar_recetas'),
    path('recetas/<str:pk>', views.RecetaDetailView.as_view(), name='receta_detail'),
]
urlpatterns +=[
  
]