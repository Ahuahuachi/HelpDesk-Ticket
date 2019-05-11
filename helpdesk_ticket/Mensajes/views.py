from django.shortcuts import render

# Create your views here.


def get_Mensaje(request):
    return render(request, 'index.html')