from django.test import TestCase, Client

from orders.management.commands.xml_read import Command
from orders.models import Orders


# Create your tests here.
class OrdersTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Orders.objects.create(
            marketplace="test",
            order_id="test1",
            order_amount=1,
            order_shipping=0,
        )
        Orders.objects.create(
            marketplace="test1",
            order_id="test1",
            order_amount=1,
            order_shipping=0,
        )

    def test_listview(self):
        response = self.client.get("/orders/")
        json_response = response.json()
        self.assertEqual(len(json_response), 2)

    def test_getview(self):
        response = self.client.get("/orders/1/")
        json_response = response.json()
        self.assertEqual(json_response["marketplace"], "test")


class OrdersXMLImport(TestCase):
    def setUp(self):
        Command().handle()

    def test_import(self):
        all_orders = Orders.objects.all()
        self.assertEqual(len(all_orders), 5)

        orders_amazon = Orders.objects.filter(marketplace="amazon")
        self.assertEqual(len(orders_amazon), 3)
