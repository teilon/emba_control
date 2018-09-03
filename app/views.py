from django.shortcuts import render
from .forms import LogInForm, ReceiptForm

from .models import Contact
from django.contrib.auth.models import User


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def login(request):
    form = LogInForm()
    context = {'form': form}

    return render(request, 'app/login.html', context)


def product(request):
    if request.method == "POST":
        [...]
    else:
        form = ReceiptForm()
        context = {'form': form}
        return render(request, 'app/productset.html', context)
