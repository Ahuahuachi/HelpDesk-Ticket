from django.shortcuts import render
from tickets.models import Ticket, Status
# Create your views here.



def get_dashboard (request):
    status = Status.objects.all().order_by('order')
    contexto = []
    for s in status:

        ticket = Ticket.objects.filter(fk_status = s)
        print(ticket, s)
        contexto.append({"name": s.status, "tickets": ticket})
    
    print (contexto)
    return render (request, 'index.html', {'status': contexto})




