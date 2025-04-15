from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def post_detalhe(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalhe.html', {'post': post})
