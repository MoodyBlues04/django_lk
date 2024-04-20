from django.urls import path
from .views import auth_views, user_views, project_views, admin_views

urlpatterns = [
    # user
    path('', user_views.home, name='home'),  # todo landing for unauthorized

    # admin
    path('admin/', admin_views.home, name='admin.home'),

    # project
    path('project/create', project_views.create, name='project.create'),

    # auth
    path('register', auth_views.register, name='register'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('email_verify', auth_views.email_verify, name='email_verify'),
]
