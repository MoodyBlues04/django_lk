from rest_framework.request import Request
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from base.helpers.auth_helpers import AuthHelper
from base.models import Tariff
from base.serializers.tariff_serializers import TariffSerializer, UpdateTariffSerializer
from django.contrib import messages


@api_view(['GET'])
def tariffs(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    _tariffs = Tariff.objects.all()

    return render(request, 'admin/tariffs.html', {'tariffs': _tariffs})


@api_view(['GET', 'POST'])
def create_tariff(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')
    if request.method == 'POST':
        serializer = TariffSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return redirect('admin.tariffs')
    return render(request, 'admin/create_tariff.html')


@api_view(['GET', 'POST'])
def edit_tariff(request: Request, tariff_id: int):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    _tariff = Tariff.objects.filter(id=tariff_id).first()
    if _tariff is None:
        messages.warning(request, 'Incorrect tariff id')
        return redirect('admin.tariffs')

    if request.method == 'POST':
        serializer = UpdateTariffSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(_tariff, serializer.data)
        return redirect('admin.tariffs')

    return render(request, 'admin/edit_tariff.html', {'tariff': _tariff})


@api_view(['GET'])
def delete_tariff(request: Request, tariff_id: int):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    _tariff = Tariff.objects.filter(id=tariff_id).first()
    if _tariff is None:
        messages.warning(request, 'Incorrect tariff id')
        return redirect('admin.tariffs')

    _tariff.delete()

    return redirect('admin.tariffs')
