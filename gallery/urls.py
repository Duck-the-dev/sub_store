from django.urls import path
from users import views




urlpatterns = [
    path('gallery', views.gallery, name='gallery'),
    path('product', views.product, name="product"),

    
]