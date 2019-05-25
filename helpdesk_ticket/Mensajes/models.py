from django.db import models
from django.contrib.auth.models import User
from tickets.models import Ticket

# Create your models here.

class Mensajes(models.Model):

    def __str__(self):
        return self.mensaje

    fk_ticket = models.ForeignKey(
        Ticket,
        null=True,
        on_delete=models.SET_NULL,
        related_name='tickets',
        # verbose_name='Ticket'

    )

    mensaje = models.TextField(null=False)

    fk_requester = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    fk_agent = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
    )

    leido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


# class Mensajes(models.Model):
#     #id_ticket = models.CharField(max_length=100)
#     #id_mensaje = models.IntegerField()
#     id_usuario_envia = models.CharField(max_length=50)
#     id_usuario_recibe = models.CharField(max_length=100)
#     mensaje = models.TextField()
#     leido = models.BooleanField()
    