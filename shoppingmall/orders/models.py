from django.db import models
from django.conf import settings

from core.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE) 
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'orders'


class OrderStatus(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'order_statuses'


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        db_table = 'order_items'
