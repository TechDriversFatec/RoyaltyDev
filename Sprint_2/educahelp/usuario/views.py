from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'signup.html')


@login_required(login_url='/login/')
def logado(request):
    return render(request, 'homelogado.html')


@login_required(login_url='/login/')
def profile_user(request):
    return render(request, 'user_profile.html')


@login_required(login_url='/login/')
def arquitetura(request):
    return render(request, 'interface_arquitetura.html')


@login_required(login_url='/login/')
def hardware(request):
    return render(request, 'interface_hardware.html')


@login_required(login_url='/login/')
def ingles(request):
    return render(request, 'interface_ingles.html')


@login_required(login_url='/login/')
def matematica(request):
    return render(request, 'interface_matematica.html')


@login_required(login_url='/login/')
def portugues(request):
    return render(request, 'interface_portugues.html')


@login_required(login_url='/login/')
def programacao(request):
    return render(request, 'interface_programacao.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')


def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Credenciais incorretas. Tente novamente!')
    return redirect('/login')
