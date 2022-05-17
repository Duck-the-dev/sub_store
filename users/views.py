from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render,reverse
from .models import Login, Signup

# Create your views here.

out_of_nav_routes = {
    "contacts": "contacts",
}


def Login(request):
    # email_adress = request.POST.get('email_address')
    # password = request.POST.get('password')
    #
    # data = Login(email_address=email_adress, password=password)
    # data.save()

    return render(request, "users/login.html", {"keys": out_of_nav_routes})


def Signup(request):
    # FirstName = request.POST.get('FirstName')
    # LastName = request.POST.get('LastName')
    # Password = request.POST.get('Password')
    # email = request.POST.get('email')
    # address = request.POST.get('address')
    # address2 = request.POST.get('address2')
    # city = request.POST.get('city')
    # state = request.POST.get('state')
    # data = Signup(FirstName=FirstName, LastName=LastName, Password=Password, email=email, address=address,
    #               address2=address2, city=city, state=state)
    # data.save()

    return render(request, "users/sign-up.html", {"keys": out_of_nav_routes})


def redirect(request):
    try:
        return HttpResponseRedirect(reverse("page"))
    except Exception as e:
        raise Http404("Page not found")
