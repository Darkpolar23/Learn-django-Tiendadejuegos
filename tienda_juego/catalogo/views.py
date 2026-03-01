from django.shortcuts import render
from catalogo.models import Juego

# Create your views here.
def listado_juegos(request):
    juegos = Juego.objects.all() #trae todos los juegos de la base de datos
    
    contexto_catalogo_juegos = {"listado_juegos": juegos}
    return render(request, "catalogo/listado_juegos.html",
                   contexto_catalogo_juegos)
