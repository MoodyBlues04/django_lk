from rest_framework.request import Request
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def home(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_admin():
        return redirect('admin.home')

    return render(request, 'user/home.html')
