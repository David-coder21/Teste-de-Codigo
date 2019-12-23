from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import RegisterForm

app_name='core'

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def contact(request):
    return render(request, 'contact.html')

def vacancies(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
          form.save()
        return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {
        'form': form
    })