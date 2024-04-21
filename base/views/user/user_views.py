from rest_framework.request import Request
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from base.models import User, FAQ
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
    return render(request, 'user/info.html')


@api_view(['GET'])
def faq(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')

    faqs = FAQ.objects.filter(is_active=True)

    if request.GET.get('search'):
        from django.db.models import Q
        faqs = faqs.filter(Q(title__contains=request.GET['search']) | Q(content__contains=request.GET['search']))

    return render(request, 'user/faq.html', {'faqs': faqs})


@api_view(['GET'])
def tariffs(request: Request):
    pass
