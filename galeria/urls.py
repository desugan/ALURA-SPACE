from .views import index, imagem
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')
]
