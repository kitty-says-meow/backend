"""
Django settings for ict_hack project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import sys

import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(BASE_DIR)

DATA_DIR = os.path.join(REPO_DIR, 'data')

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Add REPO_DIR to PYTHONPATH
sys.path.insert(0, REPO_DIR)

# Quick-start development settings - unsuitable for production
env = environ.Env(
    # set casting, default value
    DJANGO_DEBUG=(bool, False),
    DJANGO_ALLOWED_HOSTS=(list, []),
    DJANGO_CORS_ORIGIN_WHITELIST=(list, []),
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(REPO_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG')

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS')
CORS_ORIGIN_WHITELIST = env('DJANGO_CORS_ORIGIN_WHITELIST')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'corsheaders',
    'debug_toolbar',
    'django_extensions',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'imagekit',
    'rest_framework',
    'simple_history',

    'departments',
    'users',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'ict_hack.urls'

TEMPLATES = [
    {
        'BACKEND':  'django.template.backends.django.DjangoTemplates',
        'DIRS':     [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS':  {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ict_hack.interfaces.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db(default=f'sqlite:///{os.path.join(DATA_DIR, "db.sqlite3")}'),
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/api/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
STATICFILES_DIRS = []
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Media files (images, documents)
MEDIA_URL = '/api/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

# Debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

LOGGING = {
    'version':                  1,
    'disable_existing_loggers': False,
    'formatters':               {
        'verbose': {
            'format':  "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple':  {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers':                 {
        'file': {
            'level':     'ERROR',
            'class':     'logging.FileHandler',
            'filename':  os.path.join(DATA_DIR, 'error.log'),
            'formatter': 'verbose'
        },
    },
    'loggers':                  {
        'django': {
            'handlers':  ['file'],
            'propagate': True,
            'level':     'ERROR',
        }
    }
}

# Django Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'mozilla_django_oidc.contrib.drf.OIDCAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES':         (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'DEFAULT_PERMISSION_CLASSES':     (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES':       (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),
    'DEFAULT_SCHEMA_CLASS':           'ict_hack.utils.openapi.AutoSchema',
}

# Keycloak OpenID settings
KEYCLOAK_SERVER = env('KEYCLOAK_SERVER')
KEYCLOAK_REALM = env('KEYCLOAK_REALM')
KEYCLOAK_CLIENT_ID = env('KEYCLOAK_CLIENT_ID')
KEYCLOAK_CLIENT_SECRET = env('KEYCLOAK_CLIENT_SECRET')

KEYCLOAK_OPENID = f'{KEYCLOAK_SERVER}/auth/realms/{KEYCLOAK_REALM}/protocol/openid-connect'

OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_OP_JWKS_ENDPOINT = f'{KEYCLOAK_OPENID}/certs'
OIDC_RP_CLIENT_ID = KEYCLOAK_CLIENT_ID
OIDC_RP_CLIENT_SECRET = KEYCLOAK_CLIENT_SECRET

OIDC_OP_AUTHORIZATION_ENDPOINT = f'{KEYCLOAK_OPENID}/auth'
OIDC_OP_TOKEN_ENDPOINT = f'{KEYCLOAK_OPENID}/token'
OIDC_OP_USER_ENDPOINT = f'{KEYCLOAK_OPENID}/userinfo'

# drf-spectacular settings
SPECTACULAR_SETTINGS = {
    'TITLE':                    'ICT.HACK API',
    'DESCRIPTION':              'ICT.HACK API',
    'SCHEMA_PATH_PREFIX':       '/api',
    'SCHEMA_PATH_PREFIX_TRIM':  False,
    'SERVE_INCLUDE_SCHEMA':     False,
    'SWAGGER_UI_SETTINGS':      '''{
        "deepLinking": true, 
        "oauth2RedirectUrl": `${window.location.protocol}//${window.location.host}/api/static/drf_spectacular_sidecar/swagger-ui-dist/oauth2-redirect.html`,
    }''',
    'SWAGGER_UI_OAUTH2_CONFIG': {
        'clientId':                          KEYCLOAK_CLIENT_ID,
        'clientSecret':                      KEYCLOAK_CLIENT_SECRET,
        'realm':                             KEYCLOAK_REALM,
        'appName':                           KEYCLOAK_CLIENT_ID,
        'usePkceWithAuthorizationCodeGrant': True,
    },
    'COMPONENT_SPLIT_REQUEST':  True,
    'POSTPROCESSING_HOOKS':     [
        'drf_spectacular.hooks.postprocess_schema_enums',
        'drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields',
    ],
    'ENUM_NAME_OVERRIDES':      {}
}

# Authentication settings
AUTHENTICATION_BACKENDS = (
    'users.auth.KeycloakOIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'users.User'

# Sentry integration
sentry_sdk.init(
    dsn=env('SENTRY_DSN', default=None),
    debug=env('SENTRY_DEBUG', cast=bool, default=DEBUG),
    environment=env('SENTRY_ENVIRONMENT', default=None),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
