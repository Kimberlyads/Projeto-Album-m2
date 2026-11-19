import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Artista

@csrf_exempt
def api_artistas(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        artista = Artista.objects.create(
            Artista=dados["Artista"],
            Ano=dados["Ano"],
            Avaliacao=dados["Avaliacao"],
            Titulo = dados["Titulo"],
        )
        return JsonResponse({"id": artista.id}, status=201)

    artistas = list(Artista.objects.values() )
    return JsonResponse(Artista, safe=False)
