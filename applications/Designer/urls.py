from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index,name="index"),
    path('',views.Designerview,name="Designerview"),
    path('DesignerProducts/<int:id>',views.DesignerProducts,name="DesignerProducts")
]

