from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """상품 시리얼라이저"""

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields= [id]
