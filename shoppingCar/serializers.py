from rest_framework.serializers import ModelSerializer

from ecommerce.product.serializers import ProductSerializer
from .models import  *


class CartSerializer(ModelSerializer):
    class Meta:
        model= Cart
        fields = '__all__'
        

class CartProdcutsSerializer(ModelSerializer):
    cart= CartSerializer()
    products = ProductSerializer()
    class Meta:
        model=CartProducts
        fields = '__all__'
        
