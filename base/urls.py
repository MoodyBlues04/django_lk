from django.urls import path
from .views import user_views

urlpatterns = [
    path('register', user_views.register_user),
    path('login', user_views.login_user),
    path('logout', user_views.login_user, name='logout'),
    path('update-credentials', user_views.update_user_credentials),
    path('test', user_views.test)
]
