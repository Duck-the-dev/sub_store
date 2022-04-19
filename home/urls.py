from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "store"
urlpatterns = [
    path('', views.index, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('<int:page_num>', views.num_router, name="num_router"),
    # path('<str:topic>/<content>/', views.new_route),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
