from django.db import models
from django.db.models import UniqueConstraint


# Create your models here.
class Orders(models.Model):
    marketplace = models.CharField(max_length=100)
    marketplace_status = models.CharField(max_length=100, null=True)
    lengow_status = models.CharField(max_length=100, null=True)
    order_id = models.CharField(max_length=100)
    order_amount = models.FloatField()
    order_shipping = models.FloatField()
    order_datetime = models.DateTimeField(null=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=("order_id", "marketplace"),
                name="unique_per_marketplace",
            )
        ]
