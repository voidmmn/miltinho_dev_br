from django.contrib import admin
from .models import Disciplina, MaterialAula

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

@admin.register(MaterialAula)
class MaterialAulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disciplina')
    list_filter = ('disciplina',)
    search_fields = ('titulo', 'resumo')
