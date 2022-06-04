import os


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

STATIC_URL = 'static/'
STATIC_ROOT = './static/'

# Media files

MEDIA_URL = 'media/'
MEDIA_ROOT = '/media/'
