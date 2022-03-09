from django.shortcuts import render
from employee.models import Employee
from employee.forms import EmployeeForm
from .models import Administrator
from .forms import AdministratorForm

# Create your views here.

def Administrator_HomePage(request):
    return render(request, 'admin_home.html')

def AddEmployee(request):
    return render(request, 'add_employee.html')

def AddAdministrator(request):
    return render(request, 'add_administrator.html')