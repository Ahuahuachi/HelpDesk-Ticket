from django.shortcuts import render

# Create your views here.

def get_userprofile (request):
    return render (request, 'userprofile.html')

def get_editprofile (request):
    return render (request, 'editprofile.html')