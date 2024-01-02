from django.db import models

# Create your models here.
class Cart(models.Model):
    User_Name=models.ForeignKey('Users.Users',on_delete=models.CASCADE)
    Product_Name=models.ForeignKey('Product.Product',on_delete=models.CASCADE)
    Product_Qty=models.DecimalField(
        default="",max_digits=2,decimal_places=0,
    )
    Total=models.DecimalField(
        default="",max_digits=8,decimal_places=2,
    )