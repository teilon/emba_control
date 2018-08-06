from django.shortcuts import render

from .models import Contact


def index(request):
    context = {}
    return render(request, 'app/index.html', context)
