from django import forms
from .models import * # For model Form Only

# For Django Form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'
