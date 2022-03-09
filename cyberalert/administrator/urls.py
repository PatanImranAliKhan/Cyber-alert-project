from django.urls import path
from . import views

urlpatterns = [
    path('',views.Administrator_HomePage,name="admin_home"),
]