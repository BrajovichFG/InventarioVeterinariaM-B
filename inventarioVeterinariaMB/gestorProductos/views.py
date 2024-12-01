from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from gestorProductos.models import Producto, Categoria
from gestorProductos.forms import ProductoRegistroForm,CategoriaRegistroForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')


def productosData(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'productosTemplate/productos.html', data)



def categoriasData(request):
    categorias = Categoria.objects.all()
    data = {'categorias': categorias}
    return render(request, 'productosTemplate/categorias.html', data)

def productoRegistro(request):
    form = ProductoRegistroForm()
    
    if request.method == 'POST':
        form = ProductoRegistroForm(request.POST)
        if form.is_valid():
            # Guardar los datos del formulario en la base de datos
            form.save()
            return HttpResponseRedirect(reverse('productosData'))
            
    data = {'form':form}  # Paso el formulario a la plantilla
    return render(request, 'ProductosTemplate/ingresarProductos.html',data)

def eliminarProducto(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return HttpResponseRedirect(reverse('productosData'))

def editarProducto(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoRegistroForm(instance=producto)
    
    if request.method == 'POST':
        form = ProductoRegistroForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('productosData'))
            
    data = {'form':form}  # Paso el formulario a la plantilla
    return render(request, 'productosTemplate/ingresarProductos.html', data)