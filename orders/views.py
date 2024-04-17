from rest_framework import viewsets, mixins

from orders.models import Orders
from orders.serializers import OrdersSerializer


class OrdersViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):

    queryset = Orders.objects.all()
    authentication_classes = []
    serializer_class = OrdersSerializer
