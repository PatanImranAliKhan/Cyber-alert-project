from django.shortcuts import render
from django.shortcuts import redirect
from employee.forms import EmployeeForm
from employee.models import Employee
from administrator.forms import AdministratorForm
from administrator.models import Administrator

from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

def HomePage(request):
    return render(request, 'index.html')

def LoginPage(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            adm = Administrator.objects.get(email=email)
            adm_pasw = adm.password
            if check_password(password,adm_pasw):
                session['email']=email
                return redirect('/administrator')
            else:
                session['email']=None
                return render(request,'login.html',{'error':'invalid password'})
        except:
            try:
                emp = Employee.objects.get(email=email)
                emp_pasw = emp.password
                if check_password(password,emp_pasw):
                    session['email']=email
                    return redirect('/employee')
                else:
                    session['email']=None
                    return render(request,'login.html',{'error':'invalid password'})
            except:
                session['email']=None
                return render(request,'login.html',{'error':'invalid email or password'})
    return render(request,'login.html')