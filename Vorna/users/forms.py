from django import form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = form.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
