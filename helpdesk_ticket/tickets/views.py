from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Ticket
from .forms import NewTicketForm


class Tickets(View):
    """ Tickets view """

    def get(self, request, priority):
        """ Get all tickets by priority """
        tickets = Ticket.objects.filter(fk_priority=priority)
        return render(request, '', {'tickets': tickets})

    def post(self, request):
        """ Create new Ticket """
        form = NewTicketForm(request.POST)
        form.save()
        return redirect('/')
