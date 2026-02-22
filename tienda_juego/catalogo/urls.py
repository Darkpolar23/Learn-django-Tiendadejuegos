from django.urls import path
from . import views 

# Aqui estaran la urls de catalago(secundaria)

urlpatterns = [
    path("", views.listado_juegos, name="listado_juegos"),
]
