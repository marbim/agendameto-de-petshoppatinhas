from django.conf import settings
from django.db import models


class Reserva(models.Model):
    SERVICOS = [
        ('banho_tosa', 'Banho & Tosa'),
        ('veterinario', 'Veterinário'),
    ]
    TAMANHOS = [
        (1, 'Pequeno'),
        (2, 'Médio'),
        (3, 'Grande'),
    ]
    TURNOS = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservas'
    )
    servico = models.CharField('Serviço', max_length=20, choices=SERVICOS)
    nomedopet = models.CharField('Nome do pet', max_length=50)
    nomedodono = models.CharField('Nome do dono', max_length=50)
    telefone = models.CharField('Telefone', max_length=15)
    tamanho = models.PositiveSmallIntegerField('Porte do pet', choices=TAMANHOS)
    turno = models.CharField('Turno', max_length=5, choices=TURNOS)
    data = models.DateField('Data')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data', 'turno']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'{self.nomedopet} - {self.get_servico_display()} em {self.data:%d/%m/%Y}'
