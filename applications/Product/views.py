from django.shortcuts import render
from .models import Product
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

def viewproducts(request,id):
    Products = Product.objects.filter(pk=id)
    context = {
        'Products':Products
    }
    return render(request,"productdetails.html",context)
