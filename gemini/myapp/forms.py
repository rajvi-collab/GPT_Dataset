# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.widgets import ReCaptcha
from .models import UserProfile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    phone_number = forms.CharField(max_length=15)
    birthdate = forms.DateField()
    captcha = ReCaptcha()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()