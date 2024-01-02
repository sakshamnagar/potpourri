from django import forms
from .models import Contact

class contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'Email': forms.EmailInput(attrs={
                'class':'form-control',
                'style':'background-color:#F6F6F6; border: solid 3px lightgrey; height:40px;'
            }),
            'Message': forms.Textarea(attrs={
                'class':'form-control',
                'style':'background-color:#F6F6F6; border: solid 3px lightgrey;',

            })
        }
