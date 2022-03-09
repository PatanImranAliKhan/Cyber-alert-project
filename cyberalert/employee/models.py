from django.db import models

# Create your models here.
class Employee(models.Model):
    username=models.CharField(max_length=60)
    email=models.CharField(max_length=60,primary_key=True)
    mobile=models.CharField(max_length=13)
    dob=models.DateField()
    password=models.CharField(max_length=255)