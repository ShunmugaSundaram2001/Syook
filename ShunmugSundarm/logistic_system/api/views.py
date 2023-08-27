from rest_framework import viewsets
from .models import Item, Customer, DeliveryVehicle, Order
from .serializers import ItemSerializer, CustomerSerializer, DeliveryVehicleSerializer, OrderSerializer
from .models import Item, Customer, DeliveryVehicle, Order
from rest_framework import viewsets, permissions
from .serializers import ItemSerializer, CustomerSerializer, DeliveryVehicleSerializer, OrderSerializer
import uuid, random, time

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DeliveryVehicleViewSet(viewsets.ModelViewSet):
    queryset = DeliveryVehicle.objects.all()
    serializer_class = DeliveryVehicleSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
def place_order(item, customer):
    order = Order(item=item, price=item.price, customer=customer)
    order.assign_delivery_vehicle()  # Assign delivery vehicle
    order.save()
    return order

def generate_unique_invoice_id():
    timestamp = int(time.time() * 1000)  # Current time in milliseconds
    random_part = random.randint(1000, 9999)  # Random 4-digit number

    invoice_id = f'{timestamp}-{random_part}'
    return invoice_id

def create_invoice(order):
    invoice_id = generate_unique_invoice_id()
    order.generate_invoice()  # Update invoiceId in the order
    invoice = {
        'invoice_id': invoice_id,
        'customer_name': order.customer.name,
        'item_name': order.item.name,
        'price': order.price
    }
    return invoice

def mark_order_delivered(order):
    order.mark_as_delivered()
    return order