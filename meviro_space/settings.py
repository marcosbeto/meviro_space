"""
Django settings for meviro_space project.

Generated by 'django-admin startproject' using Django 1.11.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's81hilqeqxmx+7wsu%c(h#+%u11le)r9htuh*wp@5nta-e3-w5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mevirospace.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    # 'bootstrap_admin',
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #ADDED BY ME ->
        #3RD PART
    # 'localflavor',
    'rest_framework',
    'rest_framework.authtoken',
        #MY APPS
    'usuarios_meviro',
    'infra',
    # 'infra.apps.InfraAdminConfig',
    'educacao',
    'administrativo',
    'logs',
    # 'venda',
    'api',
    'contaazul'    
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

ROOT_URLCONF = 'meviro_space.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates/")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                'sort_apps': 'templatetags.sort_apps',
            }
        },
    },
]

WSGI_APPLICATION = 'meviro_space.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }, 

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'meviro_space',
    #     # 'NAME': os.path.join(BASE_DIR, 'mydb'),
    #     'USER': 'space_admin',
    #     'PASSWORD': 'orivem420',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432', # 8000 is default
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7pmkgtjs6dk5i',
        # 'NAME': os.path.join(BASE_DIR, 'mydb'),
        'USER': 'imstfgiyggwjep',
        'PASSWORD': '810fbd289c96174ff0b70ebc0103544809b782ada3c9fa2e17e6f8049fcfaa70',
        'HOST': 'ec2-54-227-246-152.compute-1.amazonaws.com',
        'PORT': '5432', # 8000 is default
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', 
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# django_heroku.settings(locals())

BOOTSTRAP_ADMIN_SIDEBAR_MENU = False

APP_ORDER = [
        'usuarios_meviro',
        # 'venda',
        'administrativo',
        'infra',
        'educacao',
        'logs',
        'api',
        'contaazul'
    ]

#CONTAAZUL DATA
CA_CLIENT_ID = 'pPIYG4rGDP11A0CHTeanFTSLeGiZNGuE'
CA_CLIENT_KEY = 'H3l6iIiNYgsYyjh6m5sWZ8WMoKL5rOBy'
REDIRECT_URI = 'https://mevirospace.herokuapp.com/admin/contaazul/token/'
    