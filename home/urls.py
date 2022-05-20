from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home import views
from home.views import Support

app_name = "store"
urlpatterns = [
    path('', views.index, name="home"),
    path('contacts/', Support.as_view(), name="contacts"),
    # path('<int:page_num>', views.num_router, name="num_router"),
    # path('<str:topic>/<content>/', views.new_route),
]
