from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Ticket, Status, Priority
from .forms import NewTicketForm


class Tickets(View):
    """ Tickets view """

    def get(self, request, priority):
        """ Get all tickets by priority """
        tickets = Ticket.objects.filter(fk_priority=priority)
        return render(request, '', {'tickets': tickets})


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
