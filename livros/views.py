from django.shortcuts import get_object_or_404, render
from .models import Livro

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/lista_livros.html', {'livros': livros})

def livro_detalhe(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livros/livro_detalhe.html', {'livro': livro})