from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from gestorProductos.models import Producto, Categoria
from gestorProductos.forms import ProductoRegistroForm,CategoriaRegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html')

@login_required
def productosData(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'productosTemplate/productos.html', data)

@login_required
def productos_list(request):
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

#def productoRegistro(request):
    form = ProductoRegistroForm()
    if request.method == 'POST':
        form = ProductoRegistroForm(request.POST)
        if form.is_valid():
            # Guardar los datos del formulario en la base de datos
            form.save()
            return HttpResponseRedirect(reverse('productosData'))
            
    data = {'form':form}  # Paso el formulario a la plantilla
    return render(request, 'ProductosTemplate/ingresarProductos.html',data)


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
    
    data = {'form': form}  # Paso el formulario a la plantilla
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
            
    data = {'form':form}  # Paso el formulario a la plantilla
    return render(request, 'productosTemplate/ingresarProductos.html', data)

#funciones para categoria
def categoriaRegistro(request):
    form = CategoriaRegistroForm()
    
    if request.method == 'POST':
        form = CategoriaRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categoriasData'))
            
    data = {'form':form}  # Paso el formulario a la plantilla
    return render(request, 'ProductosTemplate/ingresarCategorias.html',data)


def eliminarCategoria(request,id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return HttpResponseRedirect(reverse('categoriasData'))

def editarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaRegistroForm(instance=categoria)
    
    if request.method == 'POST':
        form = CategoriaRegistroForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categoriasData'))
            
    data = {'form':form}  # Paso el formulario a la plantilla
    return render(request, 'productosTemplate/ingresarCategorias.html', data)

