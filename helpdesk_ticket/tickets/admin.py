from django.contrib import admin
from tickets.models import Ticket, Status, Priority, Attachment

admin.site.register(Ticket)
admin.site.register(Status)
admin.site.register(Priority)
admin.site.register(Attachment)
