from django.db import models

# Create your models here.
class DatabasesParams(models.Model):
    name = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True) 


class isActice(models.Model): 
    active = models.BooleanField(unique=True)
    databasesparams = models.ForeignKey(DatabasesParams, on_delete=models.CASCADE)