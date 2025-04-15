from django.shortcuts import get_object_or_404, render
from .models import Disciplina

def lista_disciplinas(request):
    disciplinas = Disciplina.objects.all().order_by('titulo')  # 👈 aqui a mágica
    return render(request, 'aulas/lista_disciplinas.html', {'disciplinas': disciplinas})

def material_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    materiais = disciplina.materiais.all()
    todas_disciplinas = Disciplina.objects.all().order_by('titulo')  # 👈 aqui a mágica
    return render(request, 'aulas/material_disciplina.html', {
        'disciplina': disciplina,
        'materiais': materiais,
        'todas_disciplinas': todas_disciplinas,
    })