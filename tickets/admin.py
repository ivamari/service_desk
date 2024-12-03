from django.contrib import admin

from tickets.models.messages import Message
from tickets.models.tickets import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'created_at', 'manager')
    list_display_links = ('client',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'created_at', 'message')
    list_display_links = ('ticket',)
