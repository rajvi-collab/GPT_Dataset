from django.core.mail import send_mail

def send_verification_email(user):
    subject = 'Verify your email'
    message = f'Please click the following link to verify your email: http://yourdomain.com/verify/{user.id}/'
    from_email = 'your-email@example.com'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)