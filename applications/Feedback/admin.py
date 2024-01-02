from django.contrib import admin
from .models import Feedback
# Register your models here.

class Feedbackview(admin.ModelAdmin):
    list_display=['First_Name','Last_Name','Email']
    list_filter=['First_Name','Last_Name','Email']
    list_per_page=10
    search_fields=['First_Name','Last_Name','Email']

    def has_add_permission(self,*args,**kwargs):
        return False

    def has_change_permission(self,*args,**kwargs):
        return False


admin.site.register(Feedback,Feedbackview)