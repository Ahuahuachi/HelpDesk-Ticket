from django.forms import ModelForm
from .models import Mensajes

# Create the form class.
class MensajeForm(ModelForm):
     class Meta:
         model = Mensajes
         fields = ['fk_ticket', 'mensaje']