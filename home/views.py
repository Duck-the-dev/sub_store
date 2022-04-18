from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

routes = {

    "gallery": "gallery",
    "info": "info",
}


def index(request):
    path = request.path
    nav_items = {"keys": routes,
                 'path': path,
                 }
    return render(request, "home/index.html", context=nav_items)


def gallery(request):
    path = request.path
    nav_items = {"keys": routes,
                 'path': path,
                 }
    return render(request, "home/gallery.html", context=nav_items)


def num_router(request, page_num):
    try:
        routes_list = list(routes.keys())
        route = routes_list[page_num]
        return HttpResponseRedirect(reverse("page", args=[route]))
    except Exception as e:
        raise Http404("Page not found")


# def router(request, topic):
#     try:
#         return HttpResponse(str(routes[topic]))
#     except Exception as e:
#         raise Http404(f"Page {e} not found")

# def new_route(request, topic, content):
#     routes[topic] = content
#     return HttpResponse(f"{str(routes[topic])} {routes}")
