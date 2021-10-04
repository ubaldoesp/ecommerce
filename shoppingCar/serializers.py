from rest_framework import serializers

from product.serializers import ProductSerializer
from .models import  *


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields = '__all__'
        

class CartProdcutsSerializer(serializers.ModelSerializer):
    cart= CartSerializer()
    product = ProductSerializer()
    
    class Meta:
        model=CartProducts
        fields = '__all__'
        
