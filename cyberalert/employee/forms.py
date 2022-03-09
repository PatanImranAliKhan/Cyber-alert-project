from django import forms
from .models import Employee
from django.forms import TextInput, PasswordInput,NumberInput,EmailInput, FileInput, IntegerField, DateInput

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        widgets={
            'username': TextInput(attrs={'type':'text','placeholder':'User Name','class':'form-control','name':'username'}),
            'email': EmailInput(attrs={'type':'email','placeholder':'example@gmail.com','class':'form-control','name':'email'}),
            'mobile': TextInput(attrs={'type':'text','placeholder':'PhoneNumber','class':'form-control','name':'mobile'}),
            'dob': DateInput(attrs={'class':'form-control','name':'category','type':'date'}),
            'password': PasswordInput(attrs={'type':'password','placeholder':'Password','class':'form-control','name':'password'})
        }