from rest_framework.request import Request
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from base.helpers.auth_helpers import AuthHelper
from base.models import User, Project
from django.contrib import messages


@api_view(['GET', 'POST'])
def home(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')  # TODO middleware

    return render(request, 'admin/home.html')


def test(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    import requests
    raise ValueError(requests.get('https://google.com').text)
    from base.helpers.gsheets_service import GoogleSheetsService
    sheet_id = GoogleSheetsService.copy_avito_sheet()
    raise ValueError('success', sheet_id)



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
