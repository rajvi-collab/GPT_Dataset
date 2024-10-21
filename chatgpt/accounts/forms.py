from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class SignupForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    birthdate = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2025)))
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'birthdate', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
