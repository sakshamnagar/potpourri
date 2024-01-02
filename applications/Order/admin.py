from django.contrib import admin
from .models import Order
# Register your models here.

class Orderview(admin.ModelAdmin):
    list_display=['order_id','name','email','payment_mode']
    list_filter=['order_id','name','email','payment_mode']
    list_per_page=10
    search_fields=['order_id','name','email','payment_mode']

    #def has_add_permission(self,*args,**kwargs):
        #return False

admin.site.register(Order,Orderview)
