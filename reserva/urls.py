from django.urls import path

from . import views

urlpatterns = [
    path('agendar/', views.agendar, name='agendar'),
    path('agendar/<slug:servico>/', views.agendar, name='agendar_servico'),
    path('minha-agenda/', views.agenda, name='agenda'),
    path('minha-agenda/<int:pk>/cancelar/', views.cancelar, name='cancelar'),
]
