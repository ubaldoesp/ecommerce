from django.contrib import admin

from shoppingCar.models import Cart, CartProducts

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartProducts)