from django.contrib import admin

from.models import Producto,Categoria
from django.contrib.auth.models import User

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio','fecha_ingreso','categoria')

admin.site.register(Producto, ProductosAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Categoria, CategoriaAdmin)

