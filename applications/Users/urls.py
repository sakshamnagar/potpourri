from django.urls import path
from . import views
from .views import PasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name="index"),
    path('about/',views.about,name="aboutus"),
    path('product/',views.product,name="product"),
    path('checkout/',views.checkout,name="checkout"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('register/',views.register,name="register"),
    path('cart/',views.cart,name="cart"),
    path('logout_view/',views.logout_view,name="logout_view"),
    path('myaccount/',views.myaccount,name="myaccount"),
    path('PasswordChangeView/',PasswordChangeView.as_view(template_name='changepassword.html'),name="changepassword"),
    path('PasswordChangeView/',PasswordChangeView.as_view(template_name='password_reset_form.html'),name="changepassword"),
    path('PasswordChangeView/',PasswordChangeView.as_view(template_name='password_reset_done.html'),name="changepassword"),
    path('PasswordChangeView/',PasswordChangeView.as_view(template_name='password_reset_confirm.html'),name="changepassword"),
    path('PasswordChangeView/',PasswordChangeView.as_view(template_name='password_reset_complete.html'),name="changepassword"),


    #path('resetpassword/',views.resetpassword,name="resetpassword1"),
    #path('resetpassword/',PasswordResetView.as_view(),name="reset_password"),
    #path('insert', views.index1,name="index1"),
    #path('datadelete/', views.datadelete,name="datadelete"),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(), 
        name="password_reset_complete"),
]

