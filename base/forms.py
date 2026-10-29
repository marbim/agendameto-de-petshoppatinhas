from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Contato


class BootstrapMixin:
    """Coloca as classes do Bootstrap em todos os campos."""

    def aplicar_bootstrap(self):
        for campo in self.fields.values():
            if isinstance(campo.widget, forms.Select):
                classe = 'form-select'
            else:
                classe = 'form-control'
            campo.widget.attrs['class'] = (campo.widget.attrs.get('class', '') + ' ' + classe).strip()


class LoginForm(BootstrapMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aplicar_bootstrap()


class CadastroForm(BootstrapMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['first_name'].label = 'Seu nome'
        self.aplicar_bootstrap()


class ContatoForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('nome', 'email', 'mensagem')
        widgets = {'mensagem': forms.Textarea(attrs={'rows': 5})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aplicar_bootstrap()
