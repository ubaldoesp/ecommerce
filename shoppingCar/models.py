from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(null=False)
    total_price= models.FloatField(default=0)
    
    def __str__(self):
        return f'{str(self.user.username)}->{str(self.total_price)}'
   
    
class CartProducts(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
    
        return f'{str(self.user)}->{str(self.product.title)}' #str(self.user.username) + "" + str(self.product.title)


@receiver(pre_save, sender=CartProducts)
def correct_price(sender, **kwargs):
    cart_products= kwargs['instance']
    price_of_product= Product.objects.get(id=cart_products.product.id)
    cart_products.price = cart_products.quantity * float(price_of_product.price)
    total_cart_products = CartProducts.objects.filter(user = cart_products.user)
    cart = Cart.objects.get(id=cart_products.cart.id)
    cart.total_price= cart_products.price + cart.total_price
    cart.save()
    