from rest_framework.request import Request
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from base.models import Project
from base.serializers.project_serializers import CreateProjectSerializer
from django.contrib import messages


@api_view(['GET'])
def projects(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_admin():
        return redirect('admin.home')

    _projects = request.user.project_set.all()

    if request.GET.get('status') is not None:
        _projects = _projects.filter(status=request.GET['status'])

    return render(request, 'user/projects.html', {'projects': _projects})


@api_view(['GET', 'POST'])
def create_project(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        serializer = CreateProjectSerializer(request.user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return redirect('user.projects')

    return render(request, 'user/create_project.html')


@api_view(['POST'])
def edit_project(request: Request, project_id: int):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.data['bucket']:
        messages.warning(request, 'Incorrect bucket')
        return redirect('user.projects')

    project = Project.objects.filter(id=project_id).first()
    if project is None:
        messages.warning(request, 'Incorrect project id')
        return redirect('user.projects')

    project.bucket = request.data.get('bucket')
    project.save()

    return redirect('user.show_project', project_id=project_id)


@api_view(['GET'])
def show_project(request: Request, project_id: int):
    if not request.user.is_authenticated:
        return redirect('login')

    project = Project.objects.filter(id=project_id).first()
    if project is None:
        messages.warning(request, 'Incorrect project id')
        return redirect('user.projects')

    return render(request, 'user/show_project.html', {'project': project})
