from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_disciplinas, name='lista_disciplinas'),
    path('disciplina/<int:pk>/', views.material_disciplina, name='material_disciplina'),
]
