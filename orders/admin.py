from django.contrib import admin

from . import models
# Register your models here.


admin.site.register(models.Pizza)
admin.site.register(models.Topping)
admin.site.register(models.Client)
admin.site.register(models.Order)
admin.site.register(models.Carrito)
