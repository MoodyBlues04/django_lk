from rest_framework.request import Request
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from base.models import User, FAQ, Tariff
from base.serializers.user_serializers import UpdateUserSerializer
from django.contrib import messages
from django.db.models import Q


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
    if request.user.is_admin():
        return redirect('admin.home')

    if request.method == 'POST':
        serializer = UpdateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(request.user, serializer.data)

    return render(request, 'user/profile.html', {'professions': User.Profession.choices})


@api_view(['GET'])
def info(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'user/info.html')


@api_view(['GET'])
def faq(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')

    faqs = FAQ.objects.filter(is_active=True)

    if request.GET.get('search'):
        faqs = faqs.filter(Q(title__contains=request.GET['search']) | Q(content__contains=request.GET['search']))

    return render(request, 'user/faq.html', {'faqs': faqs})


@api_view(['GET'])
def tariffs(request: Request):
    if not request.user.is_authenticated:
        return redirect('login')

    _tariffs = Tariff.objects.all()

    return render(request, 'user/tariffs.html', {'tariffs': _tariffs})


@api_view(['GET'])
def buy_tariff(request: Request, tariff_id: int):
    if not request.user.is_authenticated:
        return redirect('login')

    tariff = Tariff.objects.filter(id=tariff_id).first()
    if tariff is None:
        messages.warning(request, 'Incorrect tariff id')
        return redirect('user.tariffs')

    # TODO create payment & redirect to payment API page
    tariff.user_set.add(request.user)
    # temporary

    return redirect('user.tariffs')

