from django.shortcuts import render

def cursos_em_breve(request):
    return render(request, 'cursos/em_breve.html')
