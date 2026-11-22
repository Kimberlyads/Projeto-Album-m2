
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

from .models import album

@csrf_exempt
def api_album (request):
    if request.method =="POST":
        dados = json.loads(request.body)
        if dados['ano'] < 1900 or dados ['ano'] > 2026:
            return JsonResponse(
                {'erro': 'Ano menor que 1900 ou maior que 2026'}, status=400
            )
        if dados['avaliacao'] <0 or dados ['avaliacao'] >10:
            return JsonResponse(
                {'erro': 'Avaliacao menor que 0 e maior que 10'}, status=400
            )
        novo_album = album.objects.create(
            titulo=dados['titulo'],
            artista=dados['artista'],
            ano=dados['ano'],
            avaliacao=dados['avaliacao'],
        )
        return JsonResponse({'id':novo_album.id} , status=201)
    albuns = list (album.objects.values())
    return JsonResponse(albuns, safe=False)

def resumo (request):
    registros = list(album.objects.values())
    if len(registros) == 0:
        return JsonResponse({
            'total':0,
            'media_avaliacao':0,
            'melhor':'',
        })
    df = pd.DataFrame(registros)
    total = len(df)
    media_calculada = df['avaliacao'].mean()
    media_avaliacao = round(float(media_calculada),2)
    ordenado = df.sort_values('avaliacao',ascending=False)
    melhor_linha = ordenado.iloc[0]
    melhor = melhor_linha['titulo']

    return JsonResponse({
        'total': total,
        'media_avaliacao': media_avaliacao,
        'melhor': melhor,
})