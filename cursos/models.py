from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cursos/', null=True, blank=True)
    link_acesso = models.URLField(null=True, blank=True)  # pode ser link para página interna ou externa
    data_publicacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo
