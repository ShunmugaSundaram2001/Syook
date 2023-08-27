from django.db import models
import random, time

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Meta:
    app_label = 'logistic_system'

class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Meta:
    app_label = 'logistic_system'

class DeliveryVehicle(models.Model):
    registrationNumber = models.CharField(max_length=20, unique=True)
    vehicleType = models.CharField(max_length=10, choices=[('bike', 'Bike'), ('truck', 'Truck')])
    city = models.CharField(max_length=100)
    activeOrdersCount = models.PositiveIntegerField(default=0)
    
class Meta:
    app_label = 'logistic_system'

class Order(models.Model):
    orderNumber = models.CharField(max_length=4, unique=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deliveryVehicle = models.ForeignKey(DeliveryVehicle, on_delete=models.SET_NULL, null=True)
    isDelivered = models.BooleanField(default=False)
    invoiceId = models.CharField(max_length=10, null=True, blank=True)
    
class Meta:
    app_label = 'logistic_system'

class Order(models.Model):
    orderNumber = models.CharField(max_length=4, unique=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deliveryVehicle = models.ForeignKey(DeliveryVehicle, on_delete=models.SET_NULL, null=True)
    isDelivered = models.BooleanField(default=False)
    invoiceId = models.CharField(max_length=10, null=True, blank=True)

    def assign_delivery_vehicle(self):
        if self.deliveryVehicle:
            return 
        
        available_vehicles = DeliveryVehicle.objects.filter(city=self.customer.city, activeOrdersCount__lt=2)

        if available_vehicles.exists():
            delivery_vehicle = available_vehicles.first()
            delivery_vehicle.activeOrdersCount += 1
            delivery_vehicle.save()

            self.deliveryVehicle = delivery_vehicle
            self.save()

    def mark_as_delivered(self):
        if self.deliveryVehicle:
            self.deliveryVehicle.activeOrdersCount -= 1
            self.deliveryVehicle.save()
        self.isDelivered = True
        self.save()

    def generate_unique_invoice_id(self):
        timestamp = int(time.time() * 1000)
        random_part = random.randint(1000, 9999)

        invoice_id = f'INV-{timestamp}-{random_part}'
        return invoice_id

    def generate_invoice(self):
        invoice_id = self.generate_unique_invoice_id()  
        self.invoiceId = invoice_id
        self.save()
        
class Meta:
    app_label = 'logistic_system'

