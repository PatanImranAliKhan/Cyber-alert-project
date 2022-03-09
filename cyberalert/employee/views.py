from django.shortcuts import render

# Create your views here.
def Employee_HomePage(request):
    return render(request, 'emp_home.html')