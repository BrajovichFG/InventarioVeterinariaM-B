from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from gestorProductos.models import Producto

def index(request):
    return render(request, 'index.html')

def productosData(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'productosTemplate/productos.html', data)