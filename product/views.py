from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from product.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from product.models import Product

# Create your views here.
    
class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Product.objects.all()
    serializer_class = ProductSerializer