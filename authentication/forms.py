from django import forms
from .models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'type': 'text',
        'autofocus': True
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'type': 'text',
        'autofocus': True
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'type': 'text',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'type': 'text',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
        ]
