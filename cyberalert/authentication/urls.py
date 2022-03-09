from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name="home"),
    path('login/',views.LoginPage,name="login"),
]