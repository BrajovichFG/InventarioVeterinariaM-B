from django.contrib import admin
from django.urls import path,include
from gestorProductos.views import index,productosData,productoRegistro,eliminarProducto


urlpatterns = [
    path('productosdata/', productosData, name='productosData'),
    path('productoRegistro/', productoRegistro, name='productoRegistro'),
    path('eliminarProducto/<int:id>/', eliminarProducto, name='eliminarProducto'),

]