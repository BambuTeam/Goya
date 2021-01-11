from orders.models import Order
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer


 
class OrderViewSet(viewsets.ModelViewSet):
    """ view Set for Orders(CRUD)"""
    queryset = Order.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer 

class OrderDetailViewSet(viewset.ModelViewSet):
    """view Set for all Order Details """
    queryset= OrderDEtail.objects.all()
    permission_classes = [
        permission.AllowAnu
    ]
    serilizer_class = OrderDetailSerializer
    

