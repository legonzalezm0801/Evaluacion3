# Importamos path de django.urls para definir las rutas
from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.productos_vista, name='productos'),
    path('', views.index, name='index'),  # Ruta para la vista principal
    path('inicio/', views.inicio, name='inicio'),  # Ruta para la vista de inicio de sesión
    path('carrito/', views.carrito, name='carrito'),  # Ruta para la vista del carrito de compras
    path('registrarse/', views.registrarse, name='registrarse'),  # Ruta para la vista de registro
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]
# Definimos las rutas y las asociamos con las vistas correspondientes
