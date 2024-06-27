from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'imagen_tag')
    search_fields = ('nombre',)

    def imagen_tag(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" width="50" height="50" />'
        return "-"
    imagen_tag.short_description = 'Imagen'
    imagen_tag.allow_tags = True

admin.site.register(Producto, ProductoAdmin)