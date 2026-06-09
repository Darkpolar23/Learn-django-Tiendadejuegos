from django.urls import path
from . import views 

#app_name = 'catalogo'

# Aqui estaran la urls de catalago(secundaria)

urlpatterns = [
    path("", views.listado_juegos, name="listado_juegos"),
    path("<int:pk>/", views.detalle_juego, name="detalle_juego"),
]
