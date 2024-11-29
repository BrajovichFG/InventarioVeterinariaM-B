from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    fecha_ingreso = models.DateField()
    categoria = models.ForeignKey(Categoria,null=True,blank=True,on_delete=models.CASCADE)

