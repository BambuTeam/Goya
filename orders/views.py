from django.shortcuts import render
from orders.models import *
from django.views.generic import ListView

# Create your views here.

class DeliveTypeList(ListView):
    model = DeliveryType
    context_object_name = 'DeliveryType'
    paginate_by = 10
    template_name='orders/delivertype_feed.html'


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
