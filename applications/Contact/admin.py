from django.contrib import admin
from .models import Contact
# Register your models here.

class Contactview(admin.ModelAdmin):
    list_display=['Name','Email','Subject']
    list_filter=['Name','Email','Subject']
    list_per_page=10
    search_fields=['Name']

    def has_add_permission(self,*args,**kwargs):
        return False

    def has_change_permission(self,*args,**kwargs):
        return False

admin.site.register(Contact,Contactview)