from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, reverse

# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

out_of_nav_routes = {
    "contacts": "contacts",
}


class Login(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = "registration/login.html"

    def get_success_url(self):
        return reverse_lazy('store:home')


# def login(request):
#
#     # email_adress = request.POST.get('email_address')
#     # password = request.POST.get('password')
#     #
#     # data = Login(email_address=email_adress, password=password)
#     # data.save()
#
#     return render(request, , {"keys": out_of_nav_routes})


def redirect(request):
    try:
        return HttpResponseRedirect(reverse("page"))
    except Exception as e:
        raise Http404("Page not found")
