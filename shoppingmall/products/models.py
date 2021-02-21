from django.db import models


class Product(models.Model):
    "상품 테이블"
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField(null=True)

    class Meta:
        db_table = 'products'
