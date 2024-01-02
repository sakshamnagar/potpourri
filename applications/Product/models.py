from django.db import models
from Designer.models import Designer

# Create your models here.
class Product(models.Model):
    Cat_Name=models.ForeignKey("Category.Category",on_delete=models.CASCADE)
    Designers_Name=models.ForeignKey(Designer,on_delete=models.SET_DEFAULT,default="",null=True,blank=True)
    name =models.CharField(max_length=35)
    image = models.ImageField(upload_to="prod_img")
    Description=models.TextField(default="")
    short_Description = models.TextField(default="")
    Additional_information = models.TextField(default="")
    Product_sku = models.CharField(max_length = 150)
    price = models.FloatField()
    Product_Qty=models.DecimalField(
        default="",max_digits=2,decimal_places=0,
    )
    
    Product_status=models.CharField(
        max_length=1,
        choices=(
            ('0','Inactive'),
            ('1','Active'),
        ),default="1"
    )

    def __str__(self):
        return self.name
