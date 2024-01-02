from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/cart_clear/<int:id>', views.cart_clear, name='cart_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear1/', views.cart_clear1, name='cart_clear1'),
  ]