from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
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


def profile(request):
    if request.method == 'POST':
        forms = UserProfileForm(instance=request.user,
                                data=request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Congrats! You have registered')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(forms.errors)
    else:
        forms = UserProfileForm(instance=request.user)
    context = {
        'title': 'Profile',
        'forms': forms
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
