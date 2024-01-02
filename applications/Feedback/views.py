
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import FeedbackForm

# Create your views here.


def feedback(request):
    forms = FeedbackForm(request.POST)
    if forms.is_valid():
        forms.save()
        return redirect('index')
    else:
        print("Error")
    return render(request,"feedback.html",{'forms':forms})