from django.urls import path
from . import views


app_name = 'page'


urlpatterns = [
    path('aboutus/', views.aboutUs, name='aboutUs'),
    path('linkedin/', views.linkedIn, name='linkedIn'),
]