from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.pagar.as_view(), name='pagar'),
    path('fecharpedido/', views.fecharPedido.as_view(), name='fecharpedido'),
    path('detalhe/', views.detalhe.as_view(), name='detalhe'),
]