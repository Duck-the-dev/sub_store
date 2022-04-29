from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Login,Signup

# Create your views here.

out_of_nav_routes = {
    "gallery": "gallery",
    "contacts": "contacts",
}


def login(request):
    email_adress = request.POST.get('email_address')
    password=request.Post.get('password')
    
    data=Login(email_address=email_adress,password=password)
    data.save()
        
    return render(request, "users/login.html")
    
    #path = request.path
    #method_items = {"keys": out_of_nav_routes,
      #              'path': path,
      #              }
    #return render(request, "users/login.html", context=method_items)


def signup(request):    
    FirstName= request.POST.get('FirstName')
    LastName=request.POST.get('LastName')
    Password=request.POST.get('password')
    address=request.POST.get('address')
    address2=request.POST.get('address2')
    city=request.POST.get('city')
    state=request.POST.get('state')
    return render(request, "users/sign-up.html")



    #path = request.path
    #method_items = {"keys": out_of_nav_routes,
    #                'path': path,
    #                }
    #return render(request, "users/sign-up.html", context=method_items)


def redirect(request):
    try:
        return HttpResponseRedirect(reverse("page"))
    except Exception as e:
        raise Http404("Page not found")
