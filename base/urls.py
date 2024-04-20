from django.urls import path
from .views import user_views

urlpatterns = [
    path('', user_views.home, name='home'),
    path('register', user_views.register, name='register'),
    path('login', user_views.login, name='login'),
    path('logout', user_views.login, name='logout'),
    path('email_verify', user_views.email_verify, name='email_verify'),
    path('test', user_views.test, name='test'),
]
