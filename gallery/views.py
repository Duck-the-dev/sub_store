from django.shortcuts import render
from .models import product



def product (request):
    return render (request, 'gallery/product.html')


def gallery (request):
    return render (request, 'gallery/gallery.html', {'pro':product.objects.all()})



