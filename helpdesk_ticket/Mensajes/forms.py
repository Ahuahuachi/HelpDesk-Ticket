from django.forms import ModelForm
from .models import Mensajes
from django import forms

# Create the form class.
class MensajeForm(ModelForm):
     class Meta:
         model = Mensajes
         fields = ['fk_ticket', 'mensaje']
         labels = {
            'fk_ticket': 'Ticket',
            'mensaje': 'Message'
        }
         widgets = {
            'mensaje': forms.Textarea(attrs={'rows':4, 'cols':100}),
        }