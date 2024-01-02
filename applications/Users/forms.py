from django.forms import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import Users

class UserProfileForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['first_name','last_name','email','username','password1','password2','Contact_No','Address']
        

    
