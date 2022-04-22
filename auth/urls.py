from django.urls import path
from auth import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "store"
urlpatterns = [
    path('login/', views.login, name="login"),
    path('sign-up/', views.sign_up, name="sign-up"),

    # path('<int:page_num>', views.num_router, name="num_router"),
    # path('<str:topic>/<content>/', views.new_route),
]
