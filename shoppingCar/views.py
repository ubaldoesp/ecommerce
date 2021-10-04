from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from ecommerce.shoppingCar.models import CartProducts
from shoppingCar.models import Cart
from product.models import Product
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
# Create your views here.

        
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user = user, ordered=False).first()
        queryset = CartProducts.objects.filter(cart=cart)
        serializer = CartProdcutsSerializer(queryset, many= True)
        print(user)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        user = request.user
        cart,_ = Cart.objects.get_or_create(user = user, ordered=False)
        product = Product.objects.get(id = data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_products = CartProducts(cart = cart,user = user,product = product, price = price , quantity=quantity)
        cart_products.save()
        
        total_price = 0
        cart_products= CartProducts.objects.filter(user = user, cart= cart.id)
        for products in  cart_products:
                total_price += products.price
        cart.total_price = total_price
        cart.save()
        
        return Response({'success':'Products added  to your cart '})
    
    def update(self,request):
        data = request.data
        cart_product = CartProducts.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_product.quantity += quantity
        cart_product.save()
        return Response('{success':'Products Update}')
         
    def delete(self,request):
        user = request.user
        data = request.data
        cart_product = CartProducts.objects.get(id= data.get('id'))
        cart_product.delete()
        cart = Cart.objects.filter(user = user , ordered = False).first()
        queryset = CartProducts.objects.filter(cart = cart)
        serializer = CartProdcutsSerializer(queryset, many=True)
        return Response(serializer.data)
