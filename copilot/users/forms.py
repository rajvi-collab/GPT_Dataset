from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import ReCaptchaField
from django_otp.forms import OTPTokenForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2024)))
    captcha = ReCaptchaField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'birthdate', 'password1', 'password2', 'captcha')

class CustomAuthenticationForm(AuthenticationForm):
    captcha = ReCaptchaField()
    
class OTPVerificationForm(OTPTokenForm):
    pass
