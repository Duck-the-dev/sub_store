from django.urls import path,include
from users import views
from django.conf import settings
from django.conf.urls.static import static

from users.views import Login

app_name = "registration"

urlpatterns = [
    path('login/', Login.as_view, name="l"),
    # path('accounts/', include('allauth.urls')),

    # path('<int:page_num>', views.num_router, name="num_router"),
    # path('<str:topic>/<content>/', views.new_route),
]
