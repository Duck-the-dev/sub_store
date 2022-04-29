from django.db import models
from numpy import False_




class Login(models.Model):
    email_address=models.CharField(max_length=80)
    password=models.CharField(max_length=20,null=False)
    
    
    
class Signup(models.Model)  :
    x = {('Giza','Giza'),('Cairo','Cairo')}
    FirstName=models.CharField(max_length=80)
    LastName=models.CharField(max_length=80)
    Password=models.CharField(max_length=20)
    address=models.TextField
    address2=models.TextField(null=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50,choices=x)