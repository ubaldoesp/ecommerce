from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=100)
    type= models.CharField(max_length=100)
    description= models.TextField()
    filename=models.ImageField()
    height = models.IntegerField()
    width = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating= models.IntegerField()
    
    def __str__(self):
        return f'{self.title}->{self.price}'