# Importamos include y path desde django.urls
from django.contrib import admin
from django.urls import include, path

# Definimos las rutas del proyecto principal y enlazamos las rutas de la aplicación polls
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para la administración de Django
    path('polls/', include('polls.urls')),  # Incluimos las rutas definidas en polls/urls.py
]