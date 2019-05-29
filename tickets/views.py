from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
from Mensajes.models import Mensajes
from Mensajes.forms import MensajeForm
from .models import Ticket
from .forms import NewTicketForm


class Tickets(View):
    """ Tickets view """

    @method_decorator(login_required)
    def get(self, request, priority):
        """ Get all tickets by priority """
        tickets = Ticket.objects.filter(fk_priority=priority)
        return render(request, '', {'tickets': tickets})


class SingleTicket(View):
    """ Single Ticket view"""

    @method_decorator(login_required)
    def get(self, request, ticket_id):
        """ Get ticket by id """
        ticket = Ticket.objects.get(id=ticket_id)
        messages = Mensajes.objects.filter(
            fk_ticket=ticket_id).order_by('-created_at')
        form = MensajeForm(initial={"fk_ticket": ticket_id})
        form.fields['fk_ticket'].widget = forms.HiddenInput()
        return render(request, 'readticketmessages.html', {'ticket': ticket, 'messages': messages, 'form': form})
        # formMensaje = form['mensaje']
        # formTicket_id = form['fk_ticket']
        # form.fk_ticket = ticket_id

    @method_decorator(login_required)
    def post(self, request, ticket_id):
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

    @method_decorator(login_required)
    def get(self, request):
        """ Get necessary data to create a new ticket """
        form = NewTicketForm(
            initial={'fk_requester': request.user})
        form.fields['fk_requester'].widget = forms.HiddenInput()
        form.fields['fk_agent'].widget = forms.HiddenInput()
        form.fields['fk_attachments'].widget = forms.HiddenInput()
        return render(request, 'new_ticket.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        """ Create new Ticket """
        form = NewTicketForm(request.POST)
        form.save()
        return redirect('/')
