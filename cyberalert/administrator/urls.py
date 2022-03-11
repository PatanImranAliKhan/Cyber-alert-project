from django.urls import path
from . import views

urlpatterns = [
    path('',views.Administrator_HomePage,name="admin_home"),
    path('add_employee',views.AddEmployee,name="addemployee"),
    path('add_admin',views.AddAdministrator,name="add_admin")
]