from django.urls import path
from users import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "store"

urlpatterns = [
    path('login/', views.login, name="login"),
    path('sign_up/', views.sign_up, name="sign_up"),

    # path('<int:page_num>', views.num_router, name="num_router"),
    # path('<str:topic>/<content>/', views.new_route),
]
