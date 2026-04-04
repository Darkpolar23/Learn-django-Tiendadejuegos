from django.shortcuts import render
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
