from django.contrib import admin
from .models import City
# Register your models here.

class Cityview(admin.ModelAdmin):
    list_display=['Name']
    list_filter=['Name']
    list_per_page=10
    search_fields=['Name']

    #def has_add_permission(self,*args,**kwargs):
        #return False

admin.site.register(City,Cityview)