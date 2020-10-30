from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


@login_required()
def arquitetura(request):
    return render(request, 'interfaces/interface_arquitetura.html')


@login_required(login_url='/accounts/login/')
def hardware(request):
    return render(request, 'interfaces/interface_hardware.html')


@login_required(login_url='/accounts/login/')
def ingles(request):
    return render(request, 'interfaces/interface_ingles.html')


@login_required(login_url='/accounts/login/')
def matematica(request):
    return render(request, 'interfaces/interface_matematica.html')


@login_required(login_url='/accounts/login/')
def portugues(request):
    return render(request, 'interfaces/interface_portugues.html')


@login_required(login_url='/accounts/login/')
def programacao(request):
    return render(request, 'interfaces/interface_programacao.html')


class adicionaraocarrinho(View):
    pass


class removerdocarrinho(View):
    pass


class contentArq(View):
    def get(self, *args, **kwargs):
        return HttpResponse('arquitetura')


class contentHad(View):
    pass


class contentIng(View):
    pass


class contentMat(View):
    pass


class contentPor(View):
    pass


class contentPro(View):
    pass

class carrinho(View):
    pass


class finalizar(View):
    pass
