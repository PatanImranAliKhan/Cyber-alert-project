from django.urls import path
from . import views

urlpatterns = [
    path('',views.Employee_HomePage,name="emp_home"),
]