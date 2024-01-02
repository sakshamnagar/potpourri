from django.contrib import admin
from .models import Category
# Register your models here.

class Categoryview(admin.ModelAdmin):
    list_display=['Cat_Name','Cat_status']
    list_filter=['Cat_Name','Cat_status']
    list_per_page=10
    search_fields=['Cat_Name']

    #def has_add_permission(self,*args,**kwargs):
        #return False

admin.site.register(Category,Categoryview)

