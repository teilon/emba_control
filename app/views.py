from django.shortcuts import render

from .models import Contact


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def login(request):
    context = {}
    return render(request, 'app/login.html', context)
