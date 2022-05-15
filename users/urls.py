from django.urls import path
from users import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "users"

urlpatterns = [
    path('login/', views.Login, name="login"),
    path('signup/', views.Signup, name="signup"),

    # path('<int:page_num>', views.num_router, name="num_router"),
    # path('<str:topic>/<content>/', views.new_route),
]
