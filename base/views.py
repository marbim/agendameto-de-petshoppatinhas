from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import CadastroForm, ContatoForm

SERVICOS = [
    {
        'slug': 'banho_tosa',
        'nome': 'Banho & Tosa',
        'descricao': 'Seu pet sempre limpinho e cheiroso',
        'icone': 'bi-droplet-half',
    },
    {
        'slug': 'veterinario',
        'nome': 'Veterinário',
        'descricao': 'A saúde do seu melhor amigo em boas mãos',
        'icone': 'bi-heart-pulse',
    },
]


def servicos(request):
    return render(request, 'base/servicos.html', {'servicos': SERVICOS})


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada! Responderemos em breve.')
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'base/contato.html', {'form': form})


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Conta criada! Já pode agendar um serviço.')
            return redirect('servicos')
    else:
        form = CadastroForm()
    return render(request, 'registration/cadastro.html', {'form': form})
