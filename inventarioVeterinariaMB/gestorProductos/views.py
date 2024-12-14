from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from gestorProductos.models import Producto, Categoria
from gestorProductos.forms import ProductoRegistroForm,CategoriaRegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def es_superususario(user):
    return user.is_superuser

def index(request):
    return render(request, 'index.html')


@login_required
def productosData(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(usuario=request.user, usuario__is_superuser=False)
    return render(request, 'productosTemplate/productos.html', {'productos': productos})

@login_required
def categoriasData(request):
    categorias = Categoria.objects.all()
    data = {'categorias': categorias}
    return render(request, 'productosTemplate/categorias.html', data)

#funciones para producto
@login_required
def productoRegistro(request):
    if request.method == 'POST':
        form = ProductoRegistroForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return HttpResponseRedirect(reverse('productosData'))
    else:
        form = ProductoRegistroForm()
    
    data = {'form': form} 
    return render(request, 'ProductosTemplate/ingresarProductos.html', data)


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
            
    data = {'form':form}  
    return render(request, 'productosTemplate/ingresarProductos.html', data)

#funciones para categoria
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .forms import CategoriaRegistroForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import CategoriaRegistroForm

def es_superusuario(user):
    return user.is_superuser

@user_passes_test(es_superusuario, login_url='home')
def categoriaRegistro(request):
    if not request.user.is_superuser:
        
        return HttpResponseRedirect(reverse('home'))

    form = CategoriaRegistroForm()
    
    if request.method == 'POST':
        form = CategoriaRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categoriasData'))
            
    data = {'form': form}
    return render(request, 'ProductosTemplate/ingresarCategorias.html', data)


def eliminarCategoria(request, id): 
    if not request.user.is_superuser: 
        messages.warning(request, 'No tienes permisos para eliminar una categoría. Debes ser un superusuario.') 
        return HttpResponseRedirect(reverse('home')) 
    categoria = Categoria.objects.get(id=id) 
    categoria.delete() 
    return HttpResponseRedirect(reverse('categoriasData'))


@user_passes_test(es_superusuario, login_url='home')
def editarCategoria(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))
    categoria = Categoria.objects.get(id=id)

    form = CategoriaRegistroForm(instance=categoria)

    if request.method == 'POST':
        form = CategoriaRegistroForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categoriasData'))


    data = {'form': form}
    return render(request, 'productosTemplate/ingresarCategorias.html', data)


