from dj_database_url import parse as parse_db_url
from prettyconf import config
from unipath import Path

from .utils import get_version

# Project Structure
BASE_DIR = Path(__file__).ancestor(3)
PROJECT_DIR = Path(__file__).ancestor(2)
FRONTEND_DIR = PROJECT_DIR.child("frontend")

# App version
APP_VERSION = get_version()

# Developer Info
DEVELOPER_NAME = config("DEVELOPER_NAME", default='Henter')
DEVELOPER_WEBSITE = config(
    "DEVELOPER_WEBSITE",
    default='https://www.henter.com.br')

# Debug & Development
DEBUG = config("DEBUG", default=False, cast=config.boolean)

# Database
default_dburl = 'sqlite:///{}/db.sqlite3'.format(PROJECT_DIR)
DATABASES = {
    'default': config(
        'DATABASE_URL',
        default=default_dburl,
        cast=parse_db_url),
}
DATABASES['default']['CONN_MAX_AGE'] = config(
    'CONN_MAX_AGE',
    cast=config.eval,
    default='500')  # always connected
DATABASES['default']['TEST'] = {
    'NAME': config(
        'TEST_DATABASE_NAME',
        default=None)
}

#  Security & Signup/Signin
ADMIN_USERNAME = config('ADMIN_USERNAME', default='admin')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=config.list)
SECRET_KEY = config(
    'SECRET_KEY',
    default='example-kn59*npHxq)G#p7VkwfZCb)RgtUWaJjfDBrEYJ6fEk9Sj$(d)Q#uZ6U##'
)

#  Media & Static
MEDIA_URL = "/media/"
MEDIA_ROOT = config('MEDIA_ROOT', default=FRONTEND_DIR.child("media"))

STATIC_URL = config('STATIC_URL', default='/static/')
STATIC_ROOT = config(
    'STATIC_ROOT', default=str(PROJECT_DIR.child('staticfiles'))
)

STATICFILES_DIRS = [
    FRONTEND_DIR.child("static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party libs
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'django_stuff',
    # Local
    'apps.core',
    'apps.book.apps.BookConfig',
)

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'bookstore_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            FRONTEND_DIR.child("templates"),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': config(
                "TEMPLATE_DEBUG",
                default=DEBUG,
                cast=config.boolean),
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore_api.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
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
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ("pt-br", "Português (Brasil)"),
    ("en", "English"),
)
LANGUAGE_CODE = 'pt-br'
LOCALE_PATHS = (
    PROJECT_DIR.child("locale"),
)

DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True

CORS_ORIGIN_ALLOW_ALL = True


# Django REST Framework
DATE_FORMAT = '%d/%m/%Y'
DATETIME_FORMAT = 'iso-8601'
DATE_INPUT_FORMATS = (
    '%m/%d/%Y', '%d/%m/%Y', '%Y-%m-%d',
    '%m-%d-%Y', '%d-%m-%Y',
)
DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d',  # '2006-10-25'
    '%d/%m/%Y',  # '25/10/2006'
    '%Y-%m-%d %H:%M',  # '2006-10-25 14:30'
    '%d/%m/%Y %H:%M',  # '25/10/2006 14:30'
    '%m/%d/%Y %H:%M',  # '10/25/2006 14:30'
    'iso-8601',
]

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    "DATE_INPUT_FORMATS": DATE_INPUT_FORMATS,
    "DATE_FORMAT": DATE_FORMAT,
    "DATETIME_INPUT_FORMATS": DATETIME_INPUT_FORMATS
}

APPEND_SLASH = False
