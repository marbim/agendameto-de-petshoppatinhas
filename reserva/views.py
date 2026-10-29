from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ReservaForm
from .models import Reserva

SLUGS_VALIDOS = {chave for chave, _ in Reserva.SERVICOS}


@login_required
def agendar(request, servico=None):
    if servico is not None and servico not in SLUGS_VALIDOS:
        return redirect('servicos')

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            messages.success(request, 'Agendamento confirmado!')
            return redirect('agenda')
    else:
        form = ReservaForm(initial={'servico': servico} if servico else None)
    return render(request, 'reserva/agendar.html', {'form': form})


@login_required
def agenda(request):
    reservas = request.user.reservas.all()
    return render(request, 'reserva/agenda.html', {'reservas': reservas})


@login_required
@require_POST
def cancelar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk, usuario=request.user)
    reserva.delete()
    messages.success(request, 'Agendamento cancelado.')
    return redirect('agenda')
