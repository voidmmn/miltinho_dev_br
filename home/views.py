from django.shortcuts import render
from blog.models import Post
from livros.models import Livro
from cursos.models import Curso
from aulas.models import Disciplina

def homepage(request):
    posts = Post.objects.all().order_by('-data_publicacao')[:3]
    livros = Livro.objects.all().order_by('-data_publicacao')[:3]
    cursos = Curso.objects.all().order_by('-data_publicacao')[:3]
    disciplinas = Disciplina.objects.all()
    todas_disciplinas = Disciplina.objects.all()  # para o sumário lateral
    
    return render(request, 'home/home.html', {
        'posts': posts,
        'livros': livros,
        'cursos': cursos,
        'disciplinas': disciplinas,
        'todas_disciplinas': todas_disciplinas,  # aqui está o segredo da sidebar        
    })
