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
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

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

STATIC_ROOT = os.path.join(BASE_DIR, "static",'static_root')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static",'media_root')#os.path.dirname(BASE_DIR) - if need to put it outside of project dir
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap'
#ADMIN_MEDIA_PREFIX = '/static/admin/'
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    #'/home/vosoditdeus/PycharmProjects/Ms/'
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
try:
    from local_settings import *
except ImportError:
    pass