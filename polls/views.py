from django.shortcuts import render
from .models import Producto

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'polls/productos.html', {'productos': productos})



# Definimos la vista para la página principal
def index(request):
    # Renderiza la plantilla Pagina1.html ubicada en templates/html
    return render(request, 'html/Pagina1.html')

# Definimos la vista para la página de inicio de sesión
def inicio(request):
    # Renderiza la plantilla InicioSesion.html ubicada en templates/html
    return render(request, 'html/InicioSesion.html')

# Definimos la vista para la página del carrito de compras
def carrito(request):
    # Renderiza la plantilla Carrito.html ubicada en templates/html
    return render(request, 'html/Carrito.html')

# Definimos la vista para la página de productos
def productos(request):
    # Renderiza la plantilla productos.html ubicada en templates/html
    return render(request, 'html/productos.html')

# Definimos la vista para la página de registro
def registrarse(request):
    # Renderiza la plantilla Registrarse.html ubicada en templates/html
    return render(request, 'html/Registrarse.html')