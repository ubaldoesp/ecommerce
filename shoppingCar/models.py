from django.db import models
from django.db.models.deletion import SET, SET_NULL
from django.utils.translation import activate
from .models import Product, User
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(null=False)
    total_price= models.FloatField(default=0)
    
    def __str__(self):
        return str(self.user.username)+""+str(self.total_price)
    
class CartProducts(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    
    def _str_(self):
        return str(self.user.username) + "" + str(self.product.title)


