from django.db import models
from phonenumbers import PhoneNumberField

class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    birthdate = models.DateField()
    password = models.CharField(max_length=128)
    two_factor_auth = models.BooleanField(default=False)