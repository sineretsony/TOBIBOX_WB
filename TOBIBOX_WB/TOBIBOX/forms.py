from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, DrawTemplates


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Такий користувач вже існує.')

        return cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Невірний логін або пароль.',
    }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise forms.ValidationError(self.error_messages['invalid_login'])

        return cleaned_data

