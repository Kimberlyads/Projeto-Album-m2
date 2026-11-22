
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import album

@csrf_exempt
def api_album (request):
    if request.method =="POST":
        dados = json.loads(request.body)

        for campo in ['titulo','artista','ano','avaliacao']:
            if campo not in dados:
                return JsonResponse(
                    {'erro': f'O campo {campo} é obrigatório'}, status=400
                )
        if dados['ano'] < 1900 or dados ['ano'] > 2026:
            return JsonResponse(
                {'erro': 'Ano deve estar entre 1900 e 2026'}, status=400
            )
        if dados['avaliacao'] < 0 or dados ['avaliacao'] > 10:
            return JsonResponse(
                {'erro': 'Avaliacao deve estar entre 0 e 10'}, status=400
            )
        novo_album= album.objects.create(
            titulo=dados['titulo'],
            artista=dados['artista'],
            ano=dados['ano'],
            avaliacao=dados['avaliacao'],
        )
        return JsonResponse ({'id': novo_album.id}, status=201)
    albuns = list(album.objects.values())
    return JsonResponse(albuns, safe=False)
def resumo (request):
    lista = list(album.objects.all())
    if len(lista) == 0:
        return JsonResponse({
            'total':0,
            'media_avaliacao':0,
            'melhor': '',
        })
    total = len(lista)
    soma = 0
    melhor = lista[0]
    for item in lista:
        soma += item.avaliacao
        if item.avaliacao > melhor.avaliacao:
            melhor = item
    media_avaliacao =round(soma / total, 2)
    return JsonResponse({
        'total':total,
        'media_avaliacao': media_avaliacao,
        'melhor': melhor.titulo,
    })