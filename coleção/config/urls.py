"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path

from albuns.views import api_album, resumo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/albuns/', api_album),
    path('api/albuns/resumo/', resumo),
]
