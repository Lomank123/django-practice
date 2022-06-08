# Authentication

AUTH_USER_MODEL = 'accounts.CustomUser'

# Login
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/auth/login/'

# Logout
LOGOUT_URL = '/auth/logout/'
LOGOUT_REDIRECT_URL = '/auth/login/'

# Sessions
# There'll be no info about cache in related tab in django-toolbar
# But if you inspect Queries you'll see that it hits db only once
# and then apparently only cache works (1 less query)
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
