from rest_framework.request import Request
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from base.helpers.auth_helpers import AuthHelper
from base.models import User, Project
from django.contrib import messages


@api_view(['GET', 'POST']) # todo not everywhere
def home(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')  # TODO middleware

    return render(request, 'admin/home.html')


@api_view(['GET', 'POST'])
def profile(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    return render(request, 'admin/home.html')


@api_view(['GET', 'POST'])
def user_projects(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    projects = Project.objects.all()

    return render(request, 'admin/projects.html', {'projects': projects})


@api_view(['GET', 'POST'])
def users(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    _users = User.objects.all()

    return render(request, 'admin/users.html', {'users': _users})
