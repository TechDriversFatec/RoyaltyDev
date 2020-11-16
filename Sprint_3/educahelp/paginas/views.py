from django.shortcuts import render
from django.views import View



def aboutUs(request):
    return render(request, 'aboutus.html')


def linkedIn(request):
    return render(request, 'linkedin.html')