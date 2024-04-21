from django.urls import path
from .views import auth_views, user_views, project_views, admin_views

urlpatterns = [
    # admin
    path('admin/faq/<int:faq_id>/edit', admin_views.edit_faq, name='admin.edit_faq'),
    path('admin/', admin_views.home, name='admin.home'),
    path('admin/profile', admin_views.profile, name='admin.profile'),  # TODO
    path('admin/projects', admin_views.projects, name='admin.projects'),  # TODO
    path('admin/faq/<int:faq_id>/delete', admin_views.delete_faq, name='admin.delete_faq'),
    path('admin/faq/create', admin_views.create_faq, name='admin.create_faq'),
    path('admin/faq', admin_views.faq, name='admin.faq'),
    path('admin/users', admin_views.users, name='admin.users'),
    path('admin/tariffs', admin_views.tariffs, name='admin.tariffs'),  # TODO

    # user
    path('', user_views.home, name='home'),  # todo landing for unauthorized

    # project
    path('project/create', project_views.create, name='project.create'),

    # auth
    path('register', auth_views.register, name='register'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('email_verify', auth_views.email_verify, name='email_verify'),
]
