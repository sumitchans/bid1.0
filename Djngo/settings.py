"""
Django settings for Djngo project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from django.conf.locale.en import formats as en_formats
en_formats.DATETIME_FORMAT = "%d/%m/%y %H:%M"
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import mimetypes
from django.conf.global_settings import STATICFILES_DIRS, STATIC_ROOT, LOGGING, MEDIA_ROOT

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


mimetypes.add_type('text/css','.css', True)
mimetypes.add_type('application/x-css','.css', True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yaz7xlqg7kl5@)colm*@twrqt9(6+b^bmyc!6$lo(ajo0nps+r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bid',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Djngo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'bid','template'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 'django.core.context_processors.request',
                 "django.core.context_processors.i18n",
                 "django.core.context_processors.media",
               "django.core.context_processors.static",
                "django.core.context_processors.tz",
            ],
        },
    },
]

WSGI_APPLICATION = 'Djngo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bid',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'loinking',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306', 
    }
}
'''
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bid',                      # Or path to database file if using sqlite3.
        'USER': 'adminQttdBlF',                      # Not used with sqlite3.
        'PASSWORD': 'Y93VXb4dQhLi',                  # Not used with sqlite3.
        'HOST': '127.12.179.2',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306', 
    }
}
'''


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR,'Djngo.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'bid': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS=(os.path.join(BASE_DIR,'bid','static','bid','css'),os.path.join(BASE_DIR,'bid','static','bid','js'),
                  os.path.join(BASE_DIR,'bid','static','bid','image'),)
