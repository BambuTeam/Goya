from orders.models import Order, OrderDetail
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer, OrderDetailSerializer


 
class OrderViewSet(viewsets.ModelViewSet):
    """ view Set for Orders(CRUD)"""
    queryset = Order.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer 


class OrderDetailViewSet(viewsets.ModelViewSet):
    """view Set for all Order Details """
    queryset= OrderDetail.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serilizer_class = OrderDetailSerializer
    

