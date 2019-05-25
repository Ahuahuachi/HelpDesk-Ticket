from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Ticket, Status, Priority
from .forms import NewTicketForm
from Mensajes.models import Mensajes


class Tickets(View):
    """ Tickets view """

    def get(self, request, priority):
        """ Get all tickets by priority """
        tickets = Ticket.objects.filter(fk_priority=priority)
        return render(request, '', {'tickets': tickets})


class SingleTicket(View):
    """ Single Ticket view"""

    def get(self, request, ticket_id):
        """ Get ticket by id """
        ticket = Ticket.objects.get(id=ticket_id)
        messages = Mensajes.objects.filter(fk_ticket=ticket_id)
        return render(request, '', {'ticket': ticket, 'messages': messages})


class NewTicket(View):
    """ View to create a new ticket """

    def get(self, request):
        """ Get necessary data to create a new ticket """
        status_list = Status.objects.all()
        priorities_list = Priority.objects.all()
        return render(request, '', {'status_list': status_list, 'priorities_list': priorities_list})

    def post(self, request):
        """ Create new Ticket """
        form = NewTicketForm(request.POST)
        form.save()
        return redirect('/')
