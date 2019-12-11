from django.db import models

# Create your models here.


class Pizza(models.Model):

    id = models.IntegerField(
        primary_key=True
    )
    product = models.CharField(
        max_length=64,
        null=False
    )
    tipe = models.CharField(
        max_length=64,
        null=False
    )
    size = models.CharField(
        max_length=64,
        null=False
    )
    price = models.FloatField(null=False)


    def __str__(self):
       return f"{self.id} - {self.product} - {self.tipe} - {self.size} - {self.price}"


class Topping(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    product = models.CharField(max_length=64, null=False,default= "")
    tipo = models.CharField(max_length=64)

#    def __str__(self):
#        return f"{self.product} - {self.tipo}"



class Client(models.Model):
    username = models.CharField(max_length=64, unique=True, primary_key=True)
    password = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64, unique=True)
    email = models.EmailField()
    logeado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} - {self.password} - {self.firstname} - {self.lastname} - {self.email}"


class Order(models.Model):
    userID = models.CharField(max_length=64) 
    productID = models.CharField(max_length=64)
    topings = models.CharField(max_length=64)
    status = models.BooleanField(default=False)
 

class Carrito(models.Model):
    productID = models.CharField(max_length=64)
    userID = models.CharField(max_length=64, null=False)
    topings = models.CharField(max_length=64)
