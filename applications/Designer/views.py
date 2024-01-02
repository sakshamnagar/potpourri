from django.shortcuts import render
from .models import Designer
from django.contrib.auth.decorators import login_required
from Product.models import Product
# Create your views here.

@login_required(login_url='adminlogin')
def Designerview(r):
        dlist = Designer.objects.filter(status=True)
        context = {
        'dlist':dlist
        }
        return render(r,"designer.html",context)





@login_required(login_url='adminlogin')
def DesignerProducts(r,id):
        plist = Product.objects.filter(Designers_Name=id)
        context = {
        'plist':plist
        }
        print(context)
        return render(r,'DesignerProducts.html',context)
        
