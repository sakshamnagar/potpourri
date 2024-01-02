from django.urls import path
from . import views

urlpatterns = [
    path('viewproducts/<int:id>',views.viewproducts,name="viewproducts"),
]


