from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from .forms import LoginForm, SignupForm
from .models import User
from recaptcha.fields import ReCaptchaField

class LoginView(APIView):
    def post(self, request):
        form = LoginForm(request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()
            if user and user.password == password:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response({'error': 'Invalid username or password'}, status=HTTP_401_UNAUTHORIZED)
        return Response({'error': 'Invalid form'}, status=HTTP_401_UNAUTHORIZED)

class SignupView(APIView):
    def post(self, request):
        form = SignupForm(request.data)
        if form.is
        
        