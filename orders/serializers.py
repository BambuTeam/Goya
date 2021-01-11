from rest_framework import serializers
from orders.models import Order, OrderDetail

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields='__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = OrderDetail
        fileds = '__all__'
    


