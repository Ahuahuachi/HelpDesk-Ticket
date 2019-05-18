from django.shortcuts import render
from django.views.generic import View
from .models import Ticket


class Tickets(View):
    """ All Tickets view """

    def get(self, request, priority):
        """ Get all tickets by priority """
        tickets = Ticket.objects.filter(fk_priority=priority)
        return render(request, '', {'tickets': tickets})
