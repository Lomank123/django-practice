import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# This will load .env file variables
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY', 'dummysecret123')

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party apps
    'rest_framework',
    'corsheaders',
    'django_cleanup',
    'django_filters',
    'debug_toolbar',
    'django_extensions',
    # Our apps
    # Here we use full path to config otherwise custom signals won't work
    'accounts.apps.AccountsConfig',
    'testapp',
    'blog',
]

MIDDLEWARE = [
    # Update cache must be the first in the list
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # Custom middlewares
    # SetUserAgentMiddleware should always go before BlockMobileMiddleware
    'main.middleware.custom.SetUserAgentMiddleware',
    'main.middleware.custom.BlockMobileMiddleware',
    'main.middleware.custom.CountRequestsMiddleware',
    'main.middleware.custom.LogTimeTakenMiddleware',

    # Fetch from cache must be the last in the list
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.custom.item_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Debug toolbar

INTERNAL_IPS = [
    '127.0.0.1',
]


def show_toolbar(request):
    return True


SHOW_TOOLBAR_CALLBACK = show_toolbar

if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)


# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
