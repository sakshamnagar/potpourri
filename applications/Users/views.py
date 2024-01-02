from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User, auth
from .forms import UserProfileForm
from Product.models import Product
from Category.models import Category
from django.contrib.auth.decorators import login_required
from Users.models import Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.template.defaulttags import register
# Model Form Select Query
@register.filter
def index(request):
    category = Category.objects.filter(Cat_status=1)
    Products = Product.objects.filter(Cat_Name="9")
    Products1 = Product.objects.filter(Cat_Name="8")
    q = request.session.items()
    
    context = {
        'Products':Products,
        'Products1':Products1,
        'category':category,
        'q':q
    }
    #object=emp2.objects.all()
    return render(request,"home.html",context)


def about(request):
    return render(request,'about.html')


def product(request):
    return render(request,"product.html")


#@login_required(login_url='adminlogin')
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('adminlogin')



# def resetpassword(request):

#     return render(request,'passwordreset.html')


def checkout(request):
    return render(request,"checkout.html")

   
  

def logout_view(request):
    logout(request)
    return redirect('index')



def adminlogin(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password'] 
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request,user)
        return redirect('index')
      else:
        return render(request,"login.html",{'msg':"Invalid Username Or password"})
   return render(request,"login.html")


def register(request):
    forms = UserProfileForm(request.POST,request.FILES)
    if forms.is_valid():
        forms.save()
        return redirect('adminlogin')
    else:
        print("Error")
    return render(request,"register.html",{'forms':forms})

def cart(request):
    return render(request,"cart.html")


@login_required(login_url='adminlogin')
def myaccount(request):
    user = request.user
    formsuser = UserProfileForm(instance=user)
    if request.method == "POST":
        if formsuser.is_valid():
            formsuser.save()
            return redirect('myaccount')
        else:
            print("Error")
    return render(request,"myaccount.html",{'formsuser':formsuser})


def ProductsList(request):
    Products = Product.objects.filter(Cat_Name="1")
    context = {
        'Products':Products
    }
    return render(request,"home.html",context)
