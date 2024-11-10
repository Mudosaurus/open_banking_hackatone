import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4lflx99$8b03bmdzs=gm^wj@gr%k2js600m*$2s(k!9w6lv1a1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['81.200.153.241', 'spacecraft-it.ru', 'localhost', '127.0.0.1', 'localhost:8080']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'e_bank',
    'style_bank',
    'consent_service',
    'hob_api',
    
    'drf_yasg',
    'rest_framework',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('POSTGRES_HOST', '81.200.153.241'),
        'NAME': os.environ.get('POSTGRES_NAME', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'PORT': int(os.environ.get('POSTGRES_PORT', '5432'))
    },
    'e_bank_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('POSTGRES_HOST', '81.200.153.241'),
        'NAME': os.environ.get('POSTGRES_EBANK_NAME', 'ebank'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'PORT': int(os.environ.get('POSTGRES_PORT', '5432'))
    },
    'style_bank_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('POSTGRES_HOST', '81.200.153.241'),
        'NAME': os.environ.get('POSTGRES_STYLEBANK_NAME', 'stylebank'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'PORT': int(os.environ.get('POSTGRES_PORT', '5432'))
    },
    'consent_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('POSTGRES_HOST', '81.200.153.241'),
        'NAME': os.environ.get('POSTGRES_CONSENT_NAME', 'consent'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'PORT': int(os.environ.get('POSTGRES_PORT', '5432'))
    }
}
DATABASE_ROUTERS = [
    'e_bank.db_router.EBankRouter',
    'style_bank.db_router.StyleBankRouter',
    'consent_service.db_router.ConsentRouter',
]


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
