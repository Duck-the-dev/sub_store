from django.urls import path
from . import views

app_name = "store"
urlpatterns = [
    path('', views.index, name="index"),
    path('gallery/', views.gallery, name="gallery"),
    path('<int:page_num>', views.num_router, name="num_router"),
    path('<str:topic>/', views.router, name="page"),
    # path('<str:topic>/<content>/', views.new_route),
]
