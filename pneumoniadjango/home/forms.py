from django import forms
from .models import *
 
 
class Form(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['xray_image'] 