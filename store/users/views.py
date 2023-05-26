from django.shortcuts import render


def registration(request):
    context = {
        'title': 'Store - registration'
    }
    return render(request, 'users/registration.html', context)


def login(request):
    context = {
        'title': 'Store - login'
    }
    return render(request, 'users/login.html', context)
