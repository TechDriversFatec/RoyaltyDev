from django.urls import path
from . import views

urlpatterns = [
    path('newcontent/', views.newContent, name='new-content')
]