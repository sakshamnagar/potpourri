from django.shortcuts import render,redirect
from .forms import contactform

# Create your views here.
def ContactUserSide(request):
    forms = contactform(request.POST)
    if request.method == "POST":
        forms = contactform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('contact')
        else:print("Error")
    return render(request,"contact.html",{'forms':forms})