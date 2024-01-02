from django.shortcuts import render
from .models import Category
from Product.models import *
from django.db.models import Q
# Create your views here.


def productview(request):
    category_list = Category.objects.filter(Cat_status="1")   
    Productview = Product.objects.all()
    contect = {
        'category_list':category_list,
        'Productview':Productview
    }
    return render(request,"category.html",contect)


def categoryForHome(request):
    category_list = Category.objects.filter(Cat_status="1")
    context = {
        'category_list':category_list
        }
    return render(request,"home.html",contect)


def ProductWithCategory(request,id):
    category_list = Category.objects.filter(Cat_status="1")
    Productview = Product.objects.filter(Cat_Name=id)
    contect = {
        'Productview':Productview,
        'category_list':category_list
    }
    return render(request,"productCategory.html",contect)

def prod_filter(request, id):
	category = Category.objects.filter(id = id)
	return render(request, 'category.html')

def search_results(request):
    if request.method == 'GET':
        
        query = request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__contains=query) | Q(Description__contains=query)
        )
        return render(request,"search.html",{'object_list':object_list})
    return render(request,"search.html",{'object_list':object_list})
