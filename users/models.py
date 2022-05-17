from django.core.validators import validate_email
from django.db import models


class Login(models.Model):
    email_address = models.EmailField(max_length=120, null=True, validators=[validate_email])
    password = models.CharField(max_length=20, null=True)


class Signup(models.Model):
    x = {('Giza', 'Giza'), ('Cairo', 'Cairo')}
    FirstName = models.CharField(max_length=80)
    LastName = models.CharField(max_length=80)
    email = models.CharField(max_length=50, null=True)
    Password = models.CharField(max_length=20)
    address = models.CharField(max_length=120)
    address2 = models.TextField(null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, choices=x)

    def __str__(self):
        return self.FirstName + ' ' + self.LastName
