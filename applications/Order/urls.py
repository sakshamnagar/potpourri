from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index,name="index"),
    path('checkout/',views.checkout,name="checkout"),
    path('OrderList/',views.OrderList,name="myorder"),
    path('bill/',views.bill,name="bill"),
]

