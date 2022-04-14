from django.urls import path
from . import views

urlpatterns = [
    path('<str:topic>/', views.router, name="home"),
    path('<str:topic>/<content>/', views.new_route),
]
