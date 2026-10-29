from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-data']
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.nome} ({self.email})'
