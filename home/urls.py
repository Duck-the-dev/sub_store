from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home import views
from home.views import SupportView, Orders, NewOrder, Index, OrderDetails, ItemUpdate, ItemDelete

app_name = "store"
urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('contacts/', SupportView.as_view(), name="contacts"),
    path("new-order/", login_required(NewOrder.as_view()), name="new-order"),
    path("orders/", login_required(Orders.as_view()), name="orders"),
    path("<int:pk>/item/", login_required(OrderDetails.as_view()), name="item"),
    path("<int:pk>/item/edit/", ItemUpdate.as_view(), name="item-update"),
    path("<int:pk>/item/delete/", ItemDelete.as_view(), name="item-delete"),
    # path('<int:page_num>', views.num_router, name="num_router"),
    # path('<str:topic>/<content>/', views.new_route),
]
