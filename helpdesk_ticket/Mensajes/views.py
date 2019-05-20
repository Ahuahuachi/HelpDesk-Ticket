from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Mensajes
from .forms import MensajeForm

# Create your views here.


def get_MensajeEntrada(request):
    mensajes = Mensajes.objects.all()
    print(mensajes)
    
    return render(request,'index.html')

def get_Mensaje(request):
    mensajes = Mensajes.objects.all()
    print(mensajes)
    
    return render(request,'readmessages.html',{'mensajes':mensajes})

def create_Mensaje(request):
    if request.method == "GET":
        form = MensajeForm()
        return render(request,'writemessage.html',{'form':form})
    elif request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mi_forma = form.save(commit=True)
            mi_forma = request.user
            mi_forma.save()
            print("DESPUES DE SALVAR")
            # form.save()
            return redirect('/Mensajes')
        else:
            print("ERROR EN CAPTURA DE MENSAJE")

    