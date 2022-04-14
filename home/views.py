from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

routes = {
    "home": "home",
    "gallery": "gallery",
    "info": "info",
}


def router(request, topic):
    return HttpResponse(routes[topic])


def new_route(request, topic,content):
    routes[topic] = content
    return HttpResponse(routes[topic])
