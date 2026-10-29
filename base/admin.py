from django.contrib import admin

from .models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data', 'lido')
    list_filter = ('lido',)
    search_fields = ('nome', 'email')
