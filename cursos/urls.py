from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos_em_breve, name='cursos_em_breve'),
]
