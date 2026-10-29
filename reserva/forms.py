import datetime

from django import forms

from base.forms import BootstrapMixin

from .models import Reserva


class ReservaForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('servico', 'nomedopet', 'nomedodono', 'telefone', 'tamanho', 'turno', 'data')
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'telefone': forms.TextInput(attrs={'placeholder': '(21) 99999-9999'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].widget.attrs['min'] = datetime.date.today().isoformat()
        self.aplicar_bootstrap()

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < datetime.date.today():
            raise forms.ValidationError('Escolha uma data a partir de hoje.')
        return data
