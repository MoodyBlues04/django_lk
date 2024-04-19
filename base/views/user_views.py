from rest_framework.response import Response
from rest_framework.request import Request
from base.serializers.user_serializers import RegisterUserSerializer, UserSerializer, LoginUserSerializer, \
    UpdateUserCredentialsSerializer
from base.error_handlers import ErrorHandler
from django.shortcuts import render


def test(request: Request):
    return render(request, 'admin_panel.html')


def register_user(request: Request):
    try:
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_serializer = UserSerializer(serializer.save())

        return Response({'success': True, 'data': user_serializer.data})
    except Exception as e:
        return ErrorHandler(e).handle()


def login_user(request: Request):
    try:
        if request.method == 'POST':

            serializer = LoginUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            user = serializer.get_authorized_user()

            return Response({'success': True})
        else:
            # TODO code for GET request
            pass
    except Exception as e:
        return ErrorHandler(e).handle()


def update_user_credentials(request: Request):
    try:
        if request.method == 'POST':
            serializer = UpdateUserCredentialsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.update_credentials()

            return Response({'success': True})
        else:
            # TODO code for GET request
            pass
    except Exception as e:
        return ErrorHandler(e).handle()
