from django import forms
from .models import Administrator
from django.forms import TextInput, PasswordInput,NumberInput,EmailInput, FileInput, IntegerField, DateInput

class AdministratorForm(forms.ModelForm):
    class Meta:
        model=Administrator
        fields='__all__'
        widgets={
            'username': TextInput(attrs={'type':'text','placeholder':'User Name','class':'form-control','name':'username'}),
            'email': EmailInput(attrs={'type':'email','placeholder':'example@gmail.com','class':'form-control','name':'email'}),
            'mobile': TextInput(attrs={'type':'text','placeholder':'PhoneNumber','class':'form-control','name':'mobile'}),
            'password': PasswordInput(attrs={'type':'password','placeholder':'Password','class':'form-control','name':'password'})
        }