"""
Django settings for cerviTestServer project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
import django_heroku
import dj_database_url
# from django.core.servers.basehttp import WSGIServer

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-+l+nul&4+o6&oog=k3y^qb(!8&^2)qx9t1_(1uqd75cz@+fav6'

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = ''

DEBUG = False
if os.getcwd() == '/app':
    DEBUG = False

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'authentication',
    'detection',
    'admin',
    'chat',
    'request',
    'rest_framework_simplejwt',
    'corsheaders',
    "anymail"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'cerviTestServer.urls'

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

WSGI_APPLICATION = 'cerviTestServer.wsgi.application'

# Suppress broken pipe errors

# WSGIServer.handle_error = lambda *args, **kwargs: None


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True


DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'

USE_L10N = False

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=15),
}

# Mail settings
# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# SENDGRID_SANDBOX_MODE_IN_DEBUG = False


# ANYMAIL = {

#     "SEND_DEFAULTS": {
#         "tags": ["app"]
#     },
#     "DEBUG_API_REQUESTS": DEBUG,
# }
# EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
# DEFAULT_FROM_EMAIL = "<your email address>"

# django_heroku.settings(locals())
# Miscellaneous patch code


# def patch_broken_pipe_error():
#     """Monkey Patch BaseServer.handle_error to not write
#     a stacktrace to stderr on broken pipe.
#     http://stackoverflow.com/a/22618740/362702"""
#     import sys
#     from socketserver import BaseServer
#     from wsgiref import handlers

#     handle_error = BaseServer.handle_error
#     log_exception = handlers.BaseHandler.log_exception

#     def is_broken_pipe_error():
#         type, err, tb = sys.exc_info()
#         return repr(err) == "error(32, 'Broken pipe')"

#     def my_handle_error(self, request, client_address):
#         if not is_broken_pipe_error():
#             handle_error(self, request, client_address)

#     def my_log_exception(self, exc_info):
#         if not is_broken_pipe_error():
#             log_exception(self, exc_info)

#     BaseServer = my_handle_error
#     handlers.BaseHandler.log_exception = my_log_exception


# patch_broken_pipe_error()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}