from rest_framework.request import Request
from base.serializers.user_serializers import RegisterUserSerializer, LoginUserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.decorators import api_view


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
    if request.method == 'POST':
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        auth_login(request, user)

        return redirect('home')

    return render(request, 'auth/register.html')


@api_view(['GET', 'POST'])
def login(request: Request):
    if request.method == 'POST':
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid()

        user = authenticate(request, email=serializer.data['email'], password=serializer.data['password'])
        if user is None:
            return redirect('login')  # TODO set flash

        return redirect('home')

    return render(request, 'auth/login.html')


