from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet

from tickets.models.tickets import Ticket
from tickets.serializers.tickets import TicketSerializer


class TicketView(GenericViewSet, mixins.ListModelMixin):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('status', )
    ordering = ('created_at', )
