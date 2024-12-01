from django import forms
from gestorProductos.models import Producto,Categoria


#editar categoria
class CategoriaRegistroForm(forms.Form):
    nombre = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    
#para crear categoria
class CategoriaRegistroForm(forms.ModelForm):
    nombre = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Categoria
        fields = ['nombre']


#para actualizar productos
class ProdudctoRegistroForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    fecha_ingreso = forms.DateField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

    nombre.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    fecha_ingreso.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'

#para registrar productos
class ProductoRegistroForm(forms.ModelForm):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    fecha_ingreso = forms.DateField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

    nombre.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    fecha_ingreso.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Producto
        fields = '__all__'