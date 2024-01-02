from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index,name="index"),
    #path('Category/',views.Categoryview,name="Categoryview"),
    path('productview/',views.productview,name="productview"),
    path('ProductWithCategory/<int:id>/',views.ProductWithCategory,name="ProductWithCategory"),
    path('search_results/',views.search_results,name="search_results"),
]

