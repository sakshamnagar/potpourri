from django.contrib import admin
from .models import Users
# Register your models here.

class Userview(admin.ModelAdmin):
    list_display=['first_name','username',]
    list_filter=['email']
    list_per_page=5
    search_fields=['email']

    #def has_add_permission(self,*args,**kwargs):
        #return False

admin.site.register(Users,Userview)

