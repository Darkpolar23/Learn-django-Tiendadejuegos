from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from catalogo.models import Juego

# Create your views here.
def listado_juegos(request):
    juegos = Juego.objects.all().order_by('id') #trae todos los juegos de la base de datos
    
    paginator = Paginator(juegos, 6) #muestra 6 juegos por pagina

    page_number  = request.GET.get('page') #obtiene el numero de pagina de la url

    page_obj = paginator.get_page(page_number) #obtiene los juegos de la pagina actual

    contexto_catalogo_juegos = {"listado_juegos": page_obj}
    
    return render(request, "catalogo/listado_juegos.html",
                   contexto_catalogo_juegos)

def detalle_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk) #obtiene el juego con el id pk o devuelve un error 404 si no existe
    
    contexto = {'juego': juego}
    
    return render(request, "catalogo/detalle_juego.html", contexto)