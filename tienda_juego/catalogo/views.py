from django.shortcuts import render

# Create your views here.
def listado_juegos(request):
    juegos = [{"nombre": "dogo racing", "precio":29.99, "plataformas": 
               ["PC", "PS4","PS5","Xbox One"]},
              {"nombre": "Naruto Strom 4", "precio":39.99, "plataformas":
               ["PC", "PS4","PS5","Xbox One"]},
              {"nombre": "Final Fantasy 15", "precio":49.99, "plataformas":
               ["PC", "PS4","PS5","Xbox One"]}, 
              {"nombre": "The Witcher 3", "precio":59.99, "plataformas":
               ["PC", "PS4","PS5","Xbox One"]},
                {"nombre": "GTA V", "precio":19.99, "plataformas":
                 ["PC", "PS4","PS5","Xbox One"]},
                {"nombre": "Red Dead Redemption 2", "precio":59.99, "plataformas":
                 ["PC", "PS4","PS5","Xbox One"]},
               ]
    
    contexto_catalogo_juegos = {"listado_juegos": juegos}
    return render(request, "catalogo/listado_juegos.html",
                   contexto_catalogo_juegos)
