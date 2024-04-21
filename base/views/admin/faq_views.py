from rest_framework.request import Request
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from base.helpers.auth_helpers import AuthHelper
from base.models import FAQ
from base.serializers.faq_serializers import FAQCreateSerializer


@api_view(['GET'])
def faq(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    faqs = FAQ.objects.all()

    return render(request, 'admin/faq.html', {'faqs': faqs})


@api_view(['GET', 'POST'])
def create_faq(request: Request):
    if not AuthHelper(request).is_admin():
        return redirect('login')
    if request.method == 'POST':
        serializer = FAQCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return redirect('admin.faq')
    return render(request, 'admin/create_faq.html')


@api_view(['GET', 'POST'])
def edit_faq(request: Request, faq_id: int):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    _faq = FAQ.objects.get(id=faq_id)
    if _faq is None:
        raise ValueError('Incorrect faq id')

    if request.method == 'POST':
        serializer = FAQCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(_faq, serializer.data)
        return redirect('admin.faq')

    return render(request, 'admin/edit_faq.html', {'faq': _faq})


@api_view(['GET'])
def delete_faq(request: Request, faq_id: int):
    if not AuthHelper(request).is_admin():
        return redirect('login')

    _faq = FAQ.objects.get(id=faq_id)
    if _faq is None:
        raise ValueError('Incorrect faq id')

    _faq.delete()

    return redirect('admin.faq')
