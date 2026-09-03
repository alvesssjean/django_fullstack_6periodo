from django.urls import path
from ..Full_Stack_Faculdade.acervo import views

urlpatterns = [
    path('livros/',
    views.lista_livros(),
    name='lista')
]
