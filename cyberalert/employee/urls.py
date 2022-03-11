from django.urls import path
from . import views

urlpatterns = [
    path('',views.Employee_HomePage,name="emp_home"),
    path('addTodo',views.AddTodoPage,name="addtodo"),
    path('viewTodo',views.ViewTodoPage,name="viewtodo"),
]