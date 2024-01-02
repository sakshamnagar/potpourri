from django.shortcuts import render,redirect
from cart.cart import Cart
from Product.models import Product
from django.template.defaulttags import register

# Create your views here.
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

def cart_clear(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

def cart_clear1(request):
    cart = Cart(request)
    cart.clear()
    return redirect("index")

@register.filter
def cart_detail(request):
    q = request.session.items()
    context = {
    'q':q
    }
    return render(request, 'cart_detail.html',context)

