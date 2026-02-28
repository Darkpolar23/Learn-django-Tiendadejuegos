from django.shortcuts import render
from catalogo.models import Juego

# Create your views here.
def listado_juegos(request):
    juegos = Juego.objects.all()
    
    contexto_catalogo_juegos = {"listado_juegos": juegos}
    return render(request, "catalogo/listado_juegos.html",
                   contexto_catalogo_juegos)
