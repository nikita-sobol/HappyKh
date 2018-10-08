"""
Django settings for happykh project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+$@f&k@)3t#@#3en0#1tatgb1draxr_34*q_g-@l56utjbkunc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = '*'

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'users.backends.UserAuthentication',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
)
# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customlogger.apps.CustomloggerConfig',
    'users.apps.UsersConfig',
    'places.apps.PlacesConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

# Basic Django REST Token setup

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'happykh.urls'

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

WSGI_APPLICATION = 'happykh.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'happykh',
        'USER': 'admin',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Logger settings
# https://docs.djangoproject.com/en/2.1/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s ::: %(levelname)s ::: %(message)s'
        },
        'file': {
            'format': '%(levelname)s ::: %(filename)s ::: %(lineno)d'
                      ' ::: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 15,
            'filename': 'logs/warnings.log',
            'formatter': 'file'
        },
        'db': {
            'level': 'CRITICAL',
            'class': 'customlogger.dbhandler.DataBaseHandler',
            'formatter': 'default'
        },
    },
    'loggers': {
        'happy_logger': {
            'handlers': ['console', 'file', 'db'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

CORS_ORIGIN_REGEX_WHITELIST = (
    # For Client
    r'http://localhost*',
    r'http://127.0.0.1:*',
    # For Testing Environment
    r'null',
)

# Email API setup

SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
