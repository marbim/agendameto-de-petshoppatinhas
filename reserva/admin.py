from django.contrib import admin

from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nomedopet', 'nomedodono', 'servico', 'data', 'turno', 'telefone')
    list_filter = ('servico', 'turno', 'data')
    search_fields = ('nomedopet', 'nomedodono', 'telefone')
