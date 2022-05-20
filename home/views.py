from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from home.forms import SupportForm
from home.models import Support

routes = {
    "contacts": "contacts",

}


class Support(CreateView):
    model = Support
    form_class = SupportForm
    # fields = '__all__'
    template_name = 'home/contacts.html'


def index(request):
    path = request.path
    nav_items = {"keys": routes,
                 'path': path,
                 }
    return render(request, "home/index.html", context=nav_items)

#


# def error_404(request, exception):
#     return render(request, '404.html', status=404)

# def router(request, topic):
#     try:
#         return HttpResponse(str(routes[topic]))
#     except Exception as e:
#         raise Http404(f"Page {e} not found")

# def new_route(request, topic, content):
#     routes[topic] = content
#     return HttpResponse(f"{str(routes[topic])} {routes}")
