import os
from main.settings.settings import BASE_DIR


# Databases and related settings

# Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'NAME': os.environ.get('DB_NAME', 'django-practice-db'),
        'USER': os.environ.get('DB_USER', 'default-user'),
        'PASSWORD': os.environ.get('DB_PASS', '12345'),
    }
}

# Static files

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Media files

MEDIA_URL = 'media/'
MEDIA_ROOT = '/media/'
