from django.shortcuts import render
from orders.models import *
from django.views.generic import ListView

# Create your views here.
#en des uso por ser codigo muerto 

class DeliveryList(ListView):
    model = Delivery
    context_object_name = Delivery
    paginate_by = 10 
    template_name = 'orders/delibery_feed.html'


class OrderList(ListView):
    model = Order
    context_object_name = Order
    paginate_by = 10 
    template_name = 'orders/order_feed.html'
