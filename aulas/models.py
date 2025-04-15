from django.db import models

class Disciplina(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=False)
    ementa = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='disciplinas/', blank=True, null=True)

    # Bibliografia Básica
    livro1_titulo = models.CharField("Livro 1", max_length=200, blank=True, null=True)
    livro1_link = models.URLField("Link Livro 1", blank=True, null=True)
    livro2_titulo = models.CharField("Livro 2", max_length=200, blank=True, null=True)
    livro2_link = models.URLField("Link Livro 2", blank=True, null=True)
    livro3_titulo = models.CharField("Livro 3", max_length=200, blank=True, null=True)
    livro3_link = models.URLField("Link Livro 3", blank=True, null=True)

    # Bibliografia Complementar
    comp1_titulo = models.CharField("Complementar 1", max_length=200, blank=True, null=True)
    comp1_link = models.URLField("Link Complementar 1", blank=True, null=True)
    comp2_titulo = models.CharField("Complementar 2", max_length=200, blank=True, null=True)
    comp2_link = models.URLField("Link Complementar 2", blank=True, null=True)
    comp3_titulo = models.CharField("Complementar 3", max_length=200, blank=True, null=True)
    comp3_link = models.URLField("Link Complementar 3", blank=True, null=True)
    comp4_titulo = models.CharField("Complementar 4", max_length=200, blank=True, null=True)
    comp4_link = models.URLField("Link Complementar 4", blank=True, null=True)
    comp5_titulo = models.CharField("Complementar 5", max_length=200, blank=True, null=True)
    comp5_link = models.URLField("Link Complementar 5", blank=True, null=True)

    def __str__(self):
        return self.titulo

class MaterialAula(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='materiais')
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    arquivo = models.FileField(upload_to='materiais/', blank=True, null=True)
    imagem = models.ImageField(upload_to='materiais/imagens/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.disciplina.titulo})"
