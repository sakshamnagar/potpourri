from django.contrib import admin
from .models import Cart
# Register your models here.

class Cartview(admin.ModelAdmin):
    list_display=['Product_Name','User_Name']
    list_filter=['Product_Name','User_Name']
    list_per_page=10
    search_fields=['Product_Name','User_Name']


    #def has_add_permission(self,*args,**kwargs):
        #return False

admin.site.register(Cart,Cartview)
