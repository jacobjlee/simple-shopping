from rest_framework import serializers

from core.models import User
from products.models import Product
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """주문 상품 시리얼라이저"""
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'quantity']
    

class OrderSerializer(serializers.ModelSerializer):
    """주문 시리얼라이저"""
    name = serializers.CharField(source='user.name', read_only=True)
    status = serializers.CharField(source='status.name', read_only=True)
    orderitem_set = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'name', 'orderitem_set', 'status', 'created_at', 'updated_at']
        read_only_fields=['id']
