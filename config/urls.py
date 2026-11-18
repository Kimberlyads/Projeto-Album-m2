from django.contrib import admin
from django.urls import path
from artistas.views import api_artistas

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/Artistas/", api_artistas),

]
