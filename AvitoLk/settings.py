"""
Django settings for AvitoLk project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
from os import getenv
import os

load_dotenv()

print(getenv('GOOGLE_API_CREDENTIALS_PATH'))
exit(0)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECURITY_KEY', 'django-insecure-heka7srlrc8f$gv(f#9cf3ov9yzo00rjw_1mbslh*oxi+k%u83')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '94.228.124.196']
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # custom
    'base',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AvitoLk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AvitoLk.wsgi.application'

# Logging


# FORMATTERS = (
#     {
#         'verbose': {
#             'format': '{levelname} {asctime:s} {threadName} {thread:d} {module} {filename} {lineno:d} {name} {funcName} {process:d} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {asctime:s} {module} {filename} {lineno:d} {funcName} {message}',
#             'style': '{',
#         },
#     },
# )
#
# HANDLERS = (
#     {
#         'console_handler': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         },
#         'my_handler': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': f'{BASE_DIR}/logs/form_parsing_log.log',
#             'mode': 'a',
#             'encoding': 'utf-8',
#             'formatter': 'simple',
#             'backupCount': 5,
#             'maxBytes': 1024 * 1024 * 5,  # 5 MB
#         },
#         'my_handler_detailed': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': f'{BASE_DIR}/logs/form_parsing_log_detailed.log',
#             'mode': 'a',
#             'formatter': 'verbose',
#             'backupCount': 5,
#             'maxBytes': 1024 * 1024 * 5,  # 5 MB
#         },
#     },
# )
#
# LOGGERS = (
#     {
#         'django': {
#             'handlers': ["console_handler", "my_handler_detailed"],
#             'level': getenv('DJANGO_LOG_LEVEL', 'INFO'),
#             'propogate': False,
#         },
#         'django.request': {
#             'handlers': ['my_handler'],
#             'level': getenv('DJANGO_REQUEST_LOG_LEVEL', 'WARNING'),
#             'propogate': False,
#         },
#     },
# )
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': FORMATTERS[0],
#     'handlers': HANDLERS[0],
#     'loggers': LOGGERS[0],
# }

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': getenv('DATABASE_ENGINE', 'django.db.backends.mysql'),
        'NAME': getenv('DATABASE_NAME', 'default_db'),
        'USER': getenv('DATABASE_USER', 'gen_user'),
        'PASSWORD': getenv('DATABASE_PASSWORD', 'tSQ1X0:zTfmqAb'),
        'HOST': getenv('DATABASE_HOST', '147.45.144.91'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Authorization
AUTH_USER_MODEL = "base.User"


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "AvitoLk/static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'base.backend.email.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_USE_TLS = False
EMAIL_PORT = 465
EMAIL_USE_SSL = True
SERVER_EMAIL = getenv('EMAIL_USERNAME', 'sokant2005@mail.ru')
DEFAULT_FROM_EMAIL = getenv('EMAIL_USERNAME', 'sokant2005@mail.ru')
EMAIL_HOST_USER = getenv('EMAIL_USERNAME', 'sokant2005@mail.ru')
EMAIL_HOST_PASSWORD = getenv('EMAIL_PASSWORD', 'jjvvwpAdai6eTp0AUv9w')
