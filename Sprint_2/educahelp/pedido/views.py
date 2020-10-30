from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('pagar')

class fecharPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('fecharPedido')

class detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detalhe')