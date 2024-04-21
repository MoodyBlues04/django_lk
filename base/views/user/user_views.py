from rest_framework.request import Request
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from base.models import User
from base.serializers.user_serializers import UpdateUserSerializer


@api_view(['GET'])
def home(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_admin():
        return redirect('admin.home')

    return render(request, 'user/home.html')


@api_view(['GET', 'POST'])
def profile(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        serializer = UpdateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(request.user, serializer.data)
    return render(request, 'user/profile.html', {'professions': User.Profession.choices})


@api_view(['GET'])
def projects(request: Request):
    pass


@api_view(['GET'])
def info(request: Request):
    pass


@api_view(['GET'])
def faq(request: Request):
    pass


@api_view(['GET'])
def tariffs(request: Request):
    pass
