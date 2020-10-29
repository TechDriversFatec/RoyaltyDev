from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario


def index(request):
    return render(request, 'home/home.html')


@login_required()
def logado(request):
    usuarios = Usuario.objects.all()
    return render(request, 'home/home.html', {'usuarios': usuarios})


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
