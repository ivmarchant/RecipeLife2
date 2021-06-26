from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vista_proveedores/', views.negocios, name='vista_proveedores'),
    path('crear_proveedor/', views.crear_negocios, name='crear_proveedor'),
    path('contacto/' ,views.contacto, name='contacto'),
    path('producto', views.producto, name='producto'),
    path('recetas', views.recetas, name='recetas'),
    path('admin', views.admin, name='admin'),
    path('preguntas',views.preguntas, name='preguntas'),
    path('registro-usuario/', views.registro_usuarios, name='registro_usuarios'),
    path('listado-usuarios/', views.listado_usuarios, name='listado_usuarios'),
    path('modificar-usuario/<id>/', views.modificar_usuario, name='modificar_usuario'),
    path('eliminar-usuarios/<id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('listado-producto/', views.listado_producto, name='listado_producto'),
    path('nuev-producto/', views.crear_producto, name='nuevo_producto'),
    path('modificar-producto/<id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
    path('negocio/<str:pk>', views.NegocioDetailView.as_view(), name='negocio_detail'),
]
urlpatterns +=[
  
]