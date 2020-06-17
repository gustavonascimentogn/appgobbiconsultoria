from __future__ import absolute_import, unicode_literals

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_(x(*#k_x5hvh0=jp=^xg-svpfp&@b8-evtjx_$ozufppgpsc!'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'apps.empresas',
    'apps.tiposServicos',
    'apps.servicos',
    'apps.clientes',
    'apps.pedidos',
    'apps.status',
    'apps.andamentos',
    'apps.contasreceber',
    'apps.solicitacoes',
    'apps.templates_mensagens',
    'apps.campanhas',
    'apps.empregados',
    'apps.arquivos',
    'apps.core',
    'apps.contaspagar',
    'apps.vendedores',
    'apps.planos_contas',
    'apps.planos_contas_grupos',

    'django_celery_results',
    'bootstrapform',
    'rest_framework',
    'rest_framework.authtoken',
    'bootstrap_datepicker_plus',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

## Configuracoes para acesso do APP a API
CORS_ORIGIN_ALLOW_ALL = True ## ativa/inativa o acesso para qualquer dominio

''' Configuracao necessaria caso CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    'localhost:80',
    'localhost:8000',
    '127.0.0.1:8000',
    'localhost:8100', ## Liberando acesso ao APP
]
'''

ROOT_URLCONF = 'gobbiconsultoria.urls'

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': ['templates'],
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
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

WSGI_APPLICATION = 'gobbiconsultoria.wsgi.application'


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

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

## STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_ROOT = (
  os.path.join(BASE_DIR, "media") #pasta media para abrigar os arquivos dos usuários
)
MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'login'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

BOOTSTRAP4 = {
    'include_jquery': True,
}

CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'


from .local_settings import  *
