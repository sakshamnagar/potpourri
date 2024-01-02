from django.contrib import admin
from .models import Product
# Register your models here.

class Productview(admin.ModelAdmin):
    list_display=['Cat_Name','name','price','Product_Qty','Product_status','Designers_Name']
    list_filter=['Cat_Name','name','price','Product_Qty','Product_status','Designers_Name']
    list_per_page=10
    search_fields=['Cat_Name','name','price','Product_Qty','Product_status','Designers_Name']
    list_editable=['Designers_Name',]

    #def has_add_permission(self,*args,**kwargs):
        #return False

admin.site.register(Product,Productview)