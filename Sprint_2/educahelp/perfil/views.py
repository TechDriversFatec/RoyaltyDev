from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('criar')


class atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('atualizar')
