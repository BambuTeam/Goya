from django.urls import path 
from orders import views


urlpatterns = [
    path(
        route ='',
        view = views.OrderList.as_view(),
        name = 'order_feed'
    ),
    path(
        route = 'delivery',
        view = views.
    ),
]
