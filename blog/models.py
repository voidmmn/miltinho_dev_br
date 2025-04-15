from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    conteudo = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='posts/', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo
