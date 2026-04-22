# me qwuede aqui haciendo el buscador de la tienda.

from django.shortcuts import render
from catalogo.models import Juego
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def buscador_juegos(request):
    query = request.GET.get('q','')

    resultados = Juego.objects.filter(
        Q(nombre__incotains = query) | Q(plataforma__incontains = query)
    ).order_by('id')

    paginator = Paginator(resultados, 6)

    page_numeber = request.GET.get('page')
    page_obj = paginator.get_page(page_numeber)

    contexto = {
        'query': query,
        'lista_juegos': page_obj 
    }

    return render(request, 'buscador/resultados_busquedas.html', contexto)