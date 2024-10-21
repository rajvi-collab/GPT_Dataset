from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import pyotp

class CustomUser(AbstractUser):
    # Add any additional fields here, but do not override groups and user_permissions
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
    
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    otp_secret = models.CharField(max_length=16, default=pyotp.random_base32, editable=False)

    def get_totp_uri(self):
        return f'otpauth://totp/MyApp:{self.username}?secret={self.otp_secret}&issuer=MyApp'

    def verify_otp(self, otp):
        totp = pyotp.TOTP(self.otp_secret)
        return totp.verify(otp)
