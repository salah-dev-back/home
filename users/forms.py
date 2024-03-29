from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'from-control', 'placeholder': 'Введите ваше имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': 'Введите ваш пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')
