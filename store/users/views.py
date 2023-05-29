from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse


def registration(request):
    if (request.method == 'POST'):
        form = UserRegistrationForm(data=request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Store - registration',
        'forms': form
    }
    return render(request, 'users/registration.html', context)


def login(request):
    if (request.method == 'POST'):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Store - login',
        'forms': form
    }
    return render(request, 'users/login.html', context)
