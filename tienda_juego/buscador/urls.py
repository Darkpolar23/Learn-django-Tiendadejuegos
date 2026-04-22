from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscador_juegos, name='bucador_juegos'),
]