from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Mensajes
from .forms import MensajeForm
from django.utils import timezone
from django.contrib.auth.models import User #,authenticate, login

from django.contrib.auth import authenticate

from django.contrib.auth import get_user

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def get_MensajeEntrada(request):
    mensajes = Mensajes.objects.all()
    # print(mensajes)
    # print(User.username)
    # print(User.first_name)
    # print(User.password)
    # print(User.email)
    # user = authenticate(username='admin', password='admin')
    # if user is not None:
    #     print("ACA")
    # else:
    #     print("NEL")

    # print("AQUI SIGUE...")
    # print(User.is_authenticated)
    # if User.is_authenticated:
    #     print("SI")
    # else:
    #     print("NO")
    
    # print(User.email)

    if request.user.is_authenticated:
        print(request.user)
    else:
        print("NO LOGEADO")

    return render(request,'index.html')

@login_required
def get_Chat(request):
    return render(request,'chat_messages.html')

@login_required
def get_Mensaje(request):
    mensajes = Mensajes.objects.all().filter(fk_requester=request.user)
    print(mensajes)
    
    return render(request,'readmessages.html',{'mensajes':mensajes})

@login_required
def create_Mensaje(request):
    if request.method == "GET":
        form = MensajeForm()
        # print(form)
        # print(form['mensaje'])
        formMensaje = form['mensaje']
        return render(request,'writemessage.html',{'form':form})
    elif request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mi_forma = form.save(commit=False)
            mi_forma.fk_requester = request.user
            mi_forma.save()
            print("DESPUES DE SALVAR")
            # form.save()
            return redirect('/Leer_Mensajes')
        else:
            print("ERROR EN CAPTURA DE MENSAJE")

    