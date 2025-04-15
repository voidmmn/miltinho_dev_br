from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('<int:pk>/', views.livro_detalhe, name='livro_detalhe'),
]
