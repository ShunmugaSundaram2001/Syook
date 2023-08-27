from rest_framework import serializers
from .models import Item, Customer, DeliveryVehicle, Order

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DeliveryVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryVehicle
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
