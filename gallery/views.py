from django.shortcuts import render
from .models import Product



def product(request):
    return render (request, 'gallery/product.html')


def gallery(request):
    return render (request, 'gallery/gallery.html', {'pro':Product.objects.all()})



