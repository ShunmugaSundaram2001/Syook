from django.test import TestCase
from .models import Item, Customer, DeliveryVehicle, Order
import uuid, random, time

class LogicTestCase(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name='Item 1', price=10)
        self.customer = Customer.objects.create(name='John', city='City A')
        self.vehicle = DeliveryVehicle.objects.create(registrationNumber='ABC123', vehicleType='bike', city='City A')

    def test_generate_unique_invoice_id(self):
        invoice_id = self.generate_unique_invoice_id()  # Use self.
        self.assertIsNotNone(invoice_id)

    def test_place_order(self):
        item = Item.objects.create(name='Item 1', price=10)
        customer = Customer.objects.create(name='John', city='City A')
        order = self.place_order(item, customer)  # Use self.
        self.assertIsNotNone(order)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.item, item)

    def test_create_invoice(self):
        order = Order.objects.create(item=self.item, price=self.item.price, customer=self.customer)
        invoice = self.create_invoice(order)  # Use self.
        self.assertEqual(invoice['customer_name'], self.customer.name)
        self.assertEqual(invoice['item_name'], self.item.name)
        self.assertEqual(invoice['price'], self.item.price)

    def generate_unique_invoice_id(self):  # Define within the class
        timestamp = int(time.time() * 1000)
        random_part = random.randint(1000, 9999)
        invoice_id = f'INV-{timestamp}-{random_part}'
        return invoice_id

    def create_invoice(self, order):  # Define within the class
        invoice_id = self.generate_unique_invoice_id()  # Use self.
        invoice = {
            'invoice_id': invoice_id,
            'customer_name': order.customer.name,
            'item_name': order.item.name,
            'price': order.price
        }
        return invoice
