from django import forms
from .models import User
from phonenumbers import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, HTML, ButtonHolder, Submit
from recaptcha.fields import ReCaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    recaptcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Login',
                Field('username'),
                Field('password'),
                HTML('<div class="g-recaptcha" data-sitekey="{}"></div>'.format(settings.RECAPTCHA_PUBLIC_KEY)),
            ),
            ButtonHolder(
                Submit('submit', 'Login')
            )
        )

class SignupForm(forms.ModelForm):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    two_factor_auth = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')])
    recaptcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'birthdate')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Signup',
                Field('username'),
                Field('email'),
                Field('phone_number'),
                Field('birthdate'),
                Field('password'),
                Field('confirm_password'),
                Field('two_factor_auth'),
                HTML('<div class="g-recaptcha" data-sitekey="{}"></div>'.format(settings.RECAPTCHA_PUBLIC_KEY)),
            ),
            ButtonHolder(
                Submit('submit', 'Signup')
            )
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')