from rest_framework.request import Request
from base.serializers.user_serializers import RegisterUserSerializer, LoginUserSerializer
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.decorators import api_view
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from datetime import datetime
from base.models import User


def test(request: Request):
    return render(request, 'admin_panel.html')
    # return render(request, 'landing.html')


@api_view(['GET', 'POST'])
def home(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'admin_panel.html')


@api_view(['GET', 'POST'])
def register(request: Request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        _send_email_verification(request, user)

        return redirect('email_verify')

    return render(request, 'auth/register.html')


def _send_email_verification(request: Request, user):
    current_site = get_current_site(request)
    subject = 'Activate Your Account'
    body = render_to_string(
        'email/verification_mail.html',
        {
            'domain': current_site.domain,
            'id': user.id,
            'token': user.email_verify_token,
        }
    )
    message = EmailMessage(subject, body, to=[user.email])
    message.content_subtype = 'html'
    message.send()


@api_view(['GET', 'POST'])
def login(request: Request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid()

        user = authenticate(request, email=serializer.data['email'], password=serializer.data['password'])
        if user is None:
            return redirect('login')  # TODO set flash
        if user.email_verified_at is None:
            return redirect('email_verify')

        auth_login(request, user)

        return redirect('home')

    return render(request, 'auth/login.html')


@api_view(['GET', 'POST'])
def email_verify(request: Request):
    if request.GET.get('id') is not None:
        user_id, token = request.GET['id'], request.GET['token']
        user = User.objects.get(id=user_id)
        if user is None or user.email_verify_token != token:
            return redirect('home')  # TODO set flash
        user.email_verified_at = datetime.now()
        user.email_verify_token = None
        user.save()
        return redirect('login')  # TODO set flash

    return render(request, 'auth/email_verify.html')


