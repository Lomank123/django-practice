# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': './main/logs/debug.log',
            'maxBytes': 1048576,
            'backupCount': 10,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'main.middleware': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        # 'propagate': True means that message will also be handled by main.middleware logger,
        # so here we write both to the console and to debug.log file.
        # If you set it to False then there'll be no messages about custom middlewares in log files
        'main.middleware.custom': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        }
    },
}
