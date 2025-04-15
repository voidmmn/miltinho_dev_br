from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),   # ← agora temos /blog/
    path('<int:pk>/', views.post_detalhe, name='post_detalhe'),
]
