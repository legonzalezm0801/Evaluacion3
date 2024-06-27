# Importamos path de django.urls para definir las rutas
from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.productos, name='productos'),
]
# Definimos las rutas y las asociamos con las vistas correspondientes
urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista principal
    path('inicio/', views.inicio, name='inicio'),  # Ruta para la vista de inicio de sesión
    path('carrito/', views.carrito, name='carrito'),  # Ruta para la vista del carrito de compras
    path('productos/', views.productos, name='productos'),  # Ruta para la vista de productos
    path('registrarse/', views.registrarse, name='registrarse'),  # Ruta para la vista de registro
]
