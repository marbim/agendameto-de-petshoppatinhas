from django.urls import path

from . import views

urlpatterns = [
    path('', views.servicos, name='servicos'),
    path('contato/', views.contato, name='contato'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
