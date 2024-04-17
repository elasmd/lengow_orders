from datetime import datetime

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.timezone import make_aware

from orders.models import Orders
from xml.etree import ElementTree


class Command(BaseCommand):
    help = "Reads xml document and inserts data into Database"

    def handle(self, *args, **options):
        parsed_xml = ElementTree.parse("orders.xml")
        root = parsed_xml.getroot()
        count_total = int(root[0].find("count_total").text)
        for item in range(count_total):
            order_item = root[1][item]
            marketplace = order_item.find("marketplace").text
            order_statuses = order_item.find("order_status")
            status_marketplace = order_statuses.find("marketplace").text
            status_lengow = order_statuses.find("lengow").text
            order_id = order_item.find("order_id").text
            order_amount = float(order_item.find("order_amount").text)
            order_shipping = float(order_item.find("order_shipping").text)
            order_date = order_item.find("order_purchase_date").text
            order_time = order_item.find("order_purchase_heure").text
            if order_time and order_date:
                order_datetime = datetime.fromisoformat(
                    f"{order_date} {order_time}"
                )
                order_datetime = make_aware(order_datetime)
            else:
                order_datetime = None
            new_order = Orders(
                marketplace=marketplace,
                marketplace_status=status_marketplace,
                lengow_status=status_lengow,
                order_id=order_id,
                order_amount=order_amount,
                order_shipping=order_shipping,
                order_datetime=order_datetime,
            )
            try:
                new_order.save()
            except IntegrityError:
                print(
                    f"Current entry is already in db {marketplace} {order_id}"
                )
