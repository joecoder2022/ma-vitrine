from django.core import validators
from django import forms
from .models import User

class SaveUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','message']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'message':forms.TextInput(attrs={'class': 'form-control'}),
        }