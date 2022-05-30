from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, TemplateView, DeleteView, UpdateView
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from home.forms import SupportForm, OrderForm
from home.models import Support, Order, IndexModel

routes = {
    "contacts": "contacts",

}


class SupportView(CreateView):
    model = Support
    form_class = SupportForm
    # fields = '__all__'
    template_name = 'home/contacts.html'


class Index(ListView):
    template_name = "home/index.html"
    model = IndexModel

    def get_context_data(self):
        context = super().get_context_data()
        context["keys"] = routes
        path = self.request.path
        context["path"] = path
        context["user"] = auth.get_user(self.request)
        return context

    def get_initial(self):
        initial_data = super(self).get_initial()
        current_user = auth.get_user(self.request).get_username()
        initial_data["username"] = current_user
        return initial_data


# https://stackoverflow.com/questions/14026750/django-model-filtering-by-user-always
class Orders(ListView, LoginRequiredMixin):
    login_url = "registration/orders.html"
    model = Order
    template_name = "home/orders.html"

    def get_queryset(self):
        return Order.objects.filter(user_id=auth.get_user(self.request).id)

    def get_success_url(self):
        return reverse("store:item")


class OrderDetails(DetailView):
    model = Order
    template_name = "home/item.html"


class ItemDelete(DeleteView):
    model = Order
    template_name = 'home/item-confirm-delete.html'
    def get_success_url(self):
        return reverse_lazy("store:orders")


class ItemUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'home/new-order.html'


    def get_success_url(self):
        return reverse("store:orders")


class NewOrder(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "home/new-order.html"

    def get_initial(self):
        initial_data = super(NewOrder, self).get_initial()
        current_user = auth.get_user(self.request)
        initial_data["user"] = current_user
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        context["keys"] = routes
        path = self.request.path
        context["path"] = path
        context["user"] = auth.get_user(self.request).get_username()
        return context
