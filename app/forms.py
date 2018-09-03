# from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from .models import ProductSet


class LogInForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'class': 'form__input', 'type': 'text'}),
            'password': TextInput(attrs={'class': 'form__input', 'type': 'password'}),
        }


class ReceiptForm(ModelForm):

    class Meta:
        model = ProductSet
        fields = ('m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm6', 'm7', 'm8', 'm8', 'm9', 'm10',
                  'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w6', 'w7', 'w8', 'w8', 'w9', 'w10',
                  'sm', 'sw', 'sd',
                  'tm', 'tw')
