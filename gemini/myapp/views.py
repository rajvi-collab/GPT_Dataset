# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignupForm, LoginForm
from .models import UserProfile
import random
import time
import datetime
import twilio.rest

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, phone_number=form.cleaned_data['phone_number'], birthdate=form.cleaned_data['birthdate'])
            # Generate OTP and send it via SMS or email
            otp = random.randint(100000, 999999)
            # Send OTP using Twilio
            client = twilio.rest.Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                to=form.cleaned_data['phone_number'],
                from_=TWILIO_PHONE_NUMBER,
                body=f"Your OTP is: {otp}"
            )
            # Store OTP in session or database for verification
            request.session['otp'] = otp
            return redirect('otp_verification')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def otp_verification(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp == request.session.get('otp'):
            # Verify OTP and log the user in
            del request.session['otp']
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP')
    return render(request, 'otp_verification.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})