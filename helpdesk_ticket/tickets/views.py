from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Ticket, Status, Priority
from .forms import NewTicketForm
from Mensajes.models import Mensajes
from Mensajes.forms import MensajeForm

from django import forms

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
        messages = Mensajes.objects.filter(fk_ticket=ticket_id).order_by('-created_at')
        form = MensajeForm(initial={"fk_ticket":ticket_id})
        form.fields['fk_ticket'].widget = forms.HiddenInput()
        

        return render(request, 'readticketmessages.html', {'ticket': ticket, 'messages': messages,'form':form})
        # formMensaje = form['mensaje']
        # formTicket_id = form['fk_ticket']
        # form.fk_ticket = ticket_id
    
    def post(self,request,ticket_id):
        form = MensajeForm(request.POST)
        if form.is_valid():
            mi_forma = form.save(commit=False)
            mi_forma.fk_requester = request.user
            mi_forma.save()
            print("DESPUES DE SALVAR")
            # form.save()
            return redirect('./'+str(ticket_id))


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
