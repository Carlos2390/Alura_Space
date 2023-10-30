from django.urls import path, include
from django.contrib import admin
from galeria.views import index, imagem, buscar

# urlpatterns = [
#     path("/admin", admin.site.urls),
#     path('', include('galeria.urls')),
# ]

urlpatterns = [
    path("", index, name= "index"),
    path('imagem/<int:foto_id>', imagem, name="imagem"),
    path("buscar", buscar, name="buscar"),
]