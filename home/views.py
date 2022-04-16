from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

routes = {
    "home": "home",
    "gallery": "gallery",
    "info": "info",
}


def index(request):
    var = {"first": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    return render(request, "home/index.html", context=var)


def num_router(request, page_num):
    try:
        routes_list = list(routes.keys())
        route = routes_list[page_num]
        return HttpResponseRedirect(reverse("page", args=[route]))
    except Exception as e:
        raise Http404("Page not found")


def router(request, topic):
    try:
        return HttpResponse(str(routes[topic]))
    except Exception as e:
        raise Http404(f"Page {e} not found")

# def new_route(request, topic, content):
#     routes[topic] = content
#     return HttpResponse(f"{str(routes[topic])} {routes}")
