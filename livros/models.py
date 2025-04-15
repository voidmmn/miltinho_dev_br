from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()  # para mostrar em listagens ou homepage
    descricao_detalhada = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='livros/', null=True, blank=True)
    link_compra = models.URLField(null=True, blank=True)
    texto_link_compra = models.CharField(max_length=200, default="Onde comprar?")
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo
