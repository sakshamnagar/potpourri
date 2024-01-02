from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from Order.models import Order
#from Product.Product import Product

@login_required(login_url='adminlogin')
def checkout(request):
	if request.method=="POST":
		items_json = request.POST.get('itemsJson', '')
		product_id = request.POST.get('product_id')
		Product_Name = request.POST.get('product_name')		
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
		city = request.POST.get('city', '')
		state = request.POST.get('state', '')
		zip_code = request.POST.get('zip_code', '')
		phone = request.POST.get('phone', '')
		product_total = request.POST.get('product_total','')
		payment_mode = request.POST.get('payment_mode')

		order = Order(items_json=items_json, name=name,product_id=product_id,Product_Name=Product_Name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code,payment_mode=payment_mode,product_total=product_total, phone=phone)
		

		order.save()
		thank = True
		id = order.order_id
		
		if payment_mode == "paytm":
			return redirect("https://paytm.com/")
		else:
			return render(request, 'thankyoupage.html', {'thank':thank, 'id': id})

		return render(request, 'thankyoupage.html', {'thank':thank, 'id': id})	
	return render(request,"checkout.html")


def OrderList(request):
	oderlist = Order.objects.filter(items_json=request.user)
	context = {
	'oderlist':oderlist
	}
	return render(request,"order.html",context)


def bill(request):
	bill_list = Order.objects.filter(items_json=request.user)
	return render(request,"inoice.html")