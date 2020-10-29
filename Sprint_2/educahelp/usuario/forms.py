# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control my-3 p-4', 'maxlengyh': 255}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-3 p-4', 'maxlengyh': 255}),
            'email': forms.TextInput(attrs={'class': 'form-control my-1 p-4', 'maxlength': 255}),
            'username': forms.TextInput(attrs={'class': 'form-control my-3 p-4', 'maxlength': 255}),
            'password': forms.PasswordInput(attrs={'class': 'form-control my-1 p-4', 'maxlength': 255}),
        }
