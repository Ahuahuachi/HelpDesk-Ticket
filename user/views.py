    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        print(request)
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('/dashboard')
        else:
            return render(request, 'registration/login.html', {'form': form})