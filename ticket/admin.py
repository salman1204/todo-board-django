from django.contrib import admin

from .models import Ticket, TicketHistory

# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    search_fields = ["title"]


admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketHistory)
