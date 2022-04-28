from django.db import models

class product(models.Model):
    name = models.CharField(max_length=100)
    content= models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    active=models.BooleanField(default=True)
    
    
    