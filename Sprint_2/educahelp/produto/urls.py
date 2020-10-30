from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('arquitetura/', views.arquitetura.as_view(), name='arquitetura'),
    path('<slug>', views.contentArq.as_view(), name='contentArq'),
    path('hardware/', views.hardware.as_view(), name='hardware'),
    path('<slug>', views.contentHad.as_view(), name='contentHad'),
    path('ingles/', views.ingles.as_view(), name='inglês'),
    path('<slug>', views.contentIng.as_view(), name='contentIng'),
    path('matematica/', views.matematica.as_view(), name='matematica'),
    path('<slug>', views.contentMat.as_view(), name='contentMat'),
    path('portugues/', views.portugues.as_view(), name='portugues'),
    path('<slug>', views.contentPor.as_view(), name='contentPor'),
    path('programacao/', views.programacao.as_view(), name='programacao'),
    path('<slug>', views.contentPro.as_view(), name='contentPro'),
    path('adicionaraocarrinho/', views.adicionaraocarrinho.as_view(), name='adicionaraocarrinho'),
    path('removerdocarrinho/', views.removerdocarrinho.as_view(), name='removerdocarrinho'),
    path('carrinho/', views.carrinho.as_view(), name='carrinho'),
    path('finalizar/', views.finalizar.as_view(), name='finalizar'),
]