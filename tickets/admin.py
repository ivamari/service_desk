from django.contrib import admin

from tickets.models.tickets import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'created_at', 'manager')
    list_display_links = ('client',)
