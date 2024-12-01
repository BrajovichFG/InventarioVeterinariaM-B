from django.contrib import admin
from django.urls import path,include
from gestorProductos.views import index,productosData,productoRegistro,eliminarProducto,categoriasData,editarProducto,categoriaRegistro,editarCategoria,eliminarCategoria


urlpatterns = [
    path('productosdata/', productosData, name='productosData'),
    path('productoRegistro/', productoRegistro, name='productoRegistro'),
    path('eliminarProducto/<int:id>/', eliminarProducto, name='eliminarProducto'),
    path('editarProducto/<int:id>/', editarProducto, name='editarProducto'),
    
    path('categoriasdata/', categoriasData, name='categoriasData'),
    path('categoriasregistro/', categoriaRegistro, name='categoriasRegistro'),
    path('eliminarCategoria/<int:id>/', eliminarCategoria, name='eliminarCategoria'),
    path('editarCategoria/<int:id>/', editarCategoria, name='editarCategoria'),

]