from django import forms
from .models import Ticket


class NewTicketForm(forms.ModelForm):
    """ New ticket form """
    class Meta:
        model = Ticket
        fields = ('subject', 'description', 'fk_status', 'fk_priority', 'fk_requester',
                  'fk_agent', 'fk_attachments')
