from django.test import APITestCase
from rest_framework import status
from product.models import Product
from .models import Cart, User, CartProducts

# Create your tests here.

class UserTests(APITestCase):
    def test_create_user(self):
        self.test.user = User.objects.create(name='Test User Name')
        
        data= {'name':self.test_user.name}
        response = self.client.post('/cart/user/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class CarTests(APITestCase):
    
    def test_create_cart_product(self):
        self.test_user= User.objects.create(name='Test User')
        self.test_product= Product.objects.create( title= 'Test Product', type='fruit', price=100, rating= 4)
        
        data = {'user':self.test_user.id,
                'product':self.test_product.id,
                'quantity':1}
        
        response= self.client.post('/cart/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cart.objects.count(),1)
        self.assertEqual(Cart.objects.get().product.title, self.test_product.title)
        
    