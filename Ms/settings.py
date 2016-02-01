"""
Django settings for MySite2_7 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# coding: utf-8
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CRISPY_TEMPLATE_PACK = 'bootstrap3'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# TODO  HIDE SECRET KEY IN local_settings.py
# SECURITY WARNING: don't run with debug turned on in production!

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party
    'registration',
    'taggit',
    'crispy_forms',
    'sorl.thumbnail',
    'redis',
    #my apps
    'photo',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'Ms.urls'

WSGI_APPLICATION = 'Ms.wsgi.application'

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static_pr","static")
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_env', 'static_root')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_env', 'media_root')
# MEDIA_ROOT = os.path.join(BASE_DIR, "static_pr","media")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_pr","static"),
    #os.path.join(os.path.dirname(BASE_DIR) "static_env"),
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

try:
    from local_settings import *
except ImportError:
    pass