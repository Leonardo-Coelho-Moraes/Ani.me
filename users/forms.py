from django import forms
from django.core.exceptions import ValidationError
from animes.templates.utilidades import campo_texto_class

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': campo_texto_class()}), label='Login:')
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': campo_texto_class()}), label='Senha:')
