from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

def productos_vista(request):
    productos = Producto.objects.all()
    return render(request, 'html/productos.html', {'productos': productos})



# Definimos la vista para la página principal
def index(request):
    # Renderiza la plantilla Pagina1.html ubicada en templates/html
    return render(request, 'html/Pagina1.html')

# Definimos la vista para la página de inicio de sesión
def inicio(request):
    # Renderiza la plantilla InicioSesion.html ubicada en templates/html
    return render(request, 'html/InicioSesion.html')


# Definimos la vista para la página de registro
def registrarse(request):
    # Renderiza la plantilla Registrarse.html ubicada en templates/html
    return render(request, 'html/Registrarse.html')

# Vista para agregar un producto al carrito
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1
    else:
        carrito[str(producto_id)] = {'nombre': producto.nombre, 'precio': str(producto.precio), 'cantidad': 1}
    request.session['carrito'] = carrito
    return redirect('carrito')

# Vista para eliminar un producto del carrito
def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito
    return redirect('carrito')

# Vista para mostrar el carrito de compras
def carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(float(item['precio']) * item['cantidad'] for item in carrito.values())
    return render(request, 'html/Carrito.html', {'carrito': carrito, 'total': total})