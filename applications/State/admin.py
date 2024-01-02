from django.contrib import admin
from .models import State
# Register your models here.

class Stateview(admin.ModelAdmin):
    list_display=['Name','Status']
    list_filter=['Name','Status']
    list_per_page=10
    search_fields=['Name','Status']

    #def has_add_permission(self,*args,**kwargs):
        #return False

admin.site.register(State,Stateview)