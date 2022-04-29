from unicodedata import category
from django.db import models
from datetime import datetime




class Product(models.Model):
    x = [('BENCHES','BENCHES'),('TABLES','TABLES'),]
    name = models.CharField(max_length=100)
    content= models.TextField(default='Foldable paper')
    category=models.CharField(max_length=50,choices=x)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    active=models.BooleanField(default=True)
    when=models.DateTimeField(auto_now_add=True)
    #datetime.now
    
    
    def __str__(self) :
        return self.name
    
    #change name of list
    class Meta :
        verbose_name='ITEMS'
    
    #change sorting of items
    class Meta:
        ordering=['-price']    
    
    