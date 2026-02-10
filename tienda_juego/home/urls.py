from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='home'), #ruta principal
    path('contacto/', views.contacto, name='contacto'), #ruta de contacto lo que hace es que llama a la vista contacto.
]
