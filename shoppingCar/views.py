from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from ecommerce.shoppingCar.models import Cart

# Create your views here.

        
class CartView(APIView):
    
    def get(self,request):
        pass
    
    def post(self,request):
        pass
    
    def update(self,request):
        pass
    
    def delete(self,request):
        pass
