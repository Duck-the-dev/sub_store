from django.shortcuts import render
from .models import Product

routes = {

    "gallery": "gallery",
    "contacts": "contacts",

}


def product(request):
    return render(request, 'gallery/product.html', {'keys': routes})


def gallery(request):
    return render(request, 'gallery/gallery.html', {'pro': Product.objects.all(), 'keys': routes, })
