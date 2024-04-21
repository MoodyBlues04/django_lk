from django.urls import path
from .views import auth_views, project_views
from .views.user import user_views, project_views
from .views.admin import admin_views, faq_views, tariff_views

urlpatterns = [
    # admin
    path('admin/', admin_views.home, name='admin.home'),
    path('admin/faq/<int:faq_id>/edit', faq_views.edit_faq, name='admin.edit_faq'),
    path('admin/faq/<int:faq_id>/delete', faq_views.delete_faq, name='admin.delete_faq'),
    path('admin/faq/create', faq_views.create_faq, name='admin.create_faq'),
    path('admin/faq', faq_views.faq, name='admin.faq'),
    path('admin/users', admin_views.users, name='admin.users'),
    path('admin/tariffs/<int:tariff_id>/edit', tariff_views.edit_tariff, name='admin.edit_tariff'),
    path('admin/tariffs/<int:tariff_id>/delete', tariff_views.delete_tariff, name='admin.delete_tariff'),
    path('admin/tariffs/create', tariff_views.create_tariff, name='admin.create_tariff'),
    path('admin/tariffs', tariff_views.tariffs, name='admin.tariffs'),

    # user
    path('', user_views.home, name='home'),  # todo landing for unauthorized
    path('profile', user_views.profile, name='user.profile'),
    path('projects', project_views.projects, name='user.projects'),
    path('info', user_views.info, name='user.info'),
    path('faq', user_views.faq, name='user.faq'),
    path('tariffs', user_views.tariffs, name='user.tariffs'), # TODO

    # project
    path('project', project_views.projects, name='user.projects'),
    path('project/create', project_views.create_project, name='user.create_project'),
    path('project/<int:project_id>', project_views.show_project, name='user.show_project'),
    path('project/<int:project_id>/edit', project_views.edit_project, name='user.edit_project'),

    # auth
    path('register', auth_views.register, name='register'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('email_verify', auth_views.email_verify, name='email_verify'),
]
