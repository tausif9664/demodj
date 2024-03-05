"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import pyodbc
SITE_ID=1
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nh$tgq@syif*h)5z70^y+90aya3q%k%iv&1a9b@0lxicug_a%t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
LOGIN_URL='/login/'
LOGIN_REDIRECT_URL = '/welcome/'
# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'workflowtest.apps.WorkflowtestConfig',
    'fcidwebsitetest.apps.FcidwebsitetestConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django_messages',
    'django.contrib.staticfiles',
    'django_filters',
    "django_tables2",
    'bootstrap_pagination',
    'bootstrap3',
'bootstrap4',
'bootstrap_datepicker_plus',
"django_ajax_tables",
    #'messages',
# "django_mutant",
'django.contrib.sites'
]
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['C:/Tausif/Ashok/FCID_ATR_22_1/FCID_ATR_22_1/users/templates',
                 os.path.join(BASE_DIR, 'templates'),
                 ],
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

WSGI_APPLICATION = 'django_project.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

            #  'ENGINE': 'sql_server.pyodbc',
            #  'NAME': 'gidcrm_qadb',
            #  'HOST': 'db1.global-id.colo',
            # 'USER': 'pip-rhiremath',
            # 'PASSWORD': 'Vmie391!',
            #  'PORT': '',
# 'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'automation',
#         'USER': 'rajesh',
#         'PASSWORD': 'rajesh',
#         'HOST': 'localhost',
#         'PORT': '3306',

     
        
            
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'users/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = 'welcome'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'rhiremath.test@gmail.com'
EMAIL_HOST_PASSWORD = 'qbzteuqfoefekntv'
# EMAIL_HOST_PASSWORD = 'nogviwthhutkxpsp'
BOOTSTRAP4 = {
    'include_jquery': True,
}