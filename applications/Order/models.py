from django.db import models
from Designer.models import Designer

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=15)
    Product_Name = models.CharField(max_length=15)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.TextField(default="")
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    payment_mode = models.CharField(max_length=150)
    product_total = models.CharField(max_length=150)