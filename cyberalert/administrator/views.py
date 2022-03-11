from django.shortcuts import render
from employee.models import Employee
from employee.forms import EmployeeForm
from .models import Administrator
from .forms import AdministratorForm
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def Administrator_HomePage(request):
    return render(request, 'admin_home.html')

def AddAdministrator(request):
    form=AdministratorForm()
    if request.method=="POST":
        request.POST._mutable = True
        request.POST['password'] = make_password(request.POST['password'],None, 'default')
        aform=AdministratorForm(request.POST)
        print(aform.errors)
        if aform.is_valid():
            aform.save()
            return render(request, 'add_administrator.html',{'form':form,'message':'Added Successfully'})
        return render(request, 'add_administrator.html',{'form':form,'error':aform.errors})
    return render(request, 'add_administrator.html',{'form':form})

def AddEmployee(request):
    form=EmployeeForm()
    if request.method=="POST":
        request.POST._mutable = True
        request.POST['password'] = make_password(request.POST['password'],None, 'default')
        eform=EmployeeForm(request.POST)
        print(eform.errors)
        if eform.is_valid():
            eform.save()
            return render(request, 'add_employee.html',{'form':form,'message':'Added Successfully'})
        return render(request, 'add_employee.html',{'form':form,'error':eform.errors})
    return render(request, 'add_employee.html',{'form':form})