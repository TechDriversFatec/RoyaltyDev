from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('arquitetura/', views.arquitetura),
    path('hardware/', views.hardware),
    path('ingles/', views.ingles),
    path('matematica/', views.matematica),
    path('portugues/', views.portugues),
    path('programacao/', views.programacao),
]