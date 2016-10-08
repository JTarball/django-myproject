#!/usr/bin/env python
"""
    settings.local
    ==============

    This is the settings file that you use when you're working on the project locally.
    Local development-specific settings include DEBUG mode, log level and activation of developer
    tools like django-debug-toolbar.
"""
from .base import *

# As of Django 1.5 all logging messages reaching the django logger are sent to Console if (DEBUG=True)
DEBUG = True

INSTALLED_APPS += (
   "djrill",
)

MANDRILL_API_KEY = "IogTH4DrRI2ZzC-n1zxuhQ"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
DEFAULT_FROM_EMAIL = "you@example.com"

# In case there are problems with whitenoise - try uncommenting the line below
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

ALLOWED_HOSTS += ['192.168.99.100', 'app']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(created)f %(filename)s %(funcName)s %(levelname)s %(module)s %(pathname)s %(process)d %(processName)s  %(lineno)s %(levelno)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'custom': {
            '()':  logger.DjangoProjectLogFormatter,
        },
        'colored': {
            '()': 'project.utils.colorlog.ColoredFormatter',
            'format': '%(log_color)s%(asctime)s %(levelname)-8s %(name)s  %(message)s',
            'log_colors': {
                'DEBUG':    'green',
                #'INFO':     'white',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'purple',
            }
        },
    },
    # special filter: e.g. only log when debug=False (Django only provides two filters) (make a custom if needed)
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         }
    },
    'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'when': 'midnight',
                'interval': 1,
                'backupCount': 30,
                'filename': SITE_ROOT + '/log/' + 'project' + '.log',
                'formatter': 'custom',
            },
            'development_logfile': {
                'level': 'DEBUG',
                'formatter': 'custom',
                'class': 'project.utils.handlers.GenRotatingFileHandler',
                'base_filename': SITE_ROOT + '/log/' + 'project',
                'suffix_filename': 'log',
                'when': 'h',
            },
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'custom',
                'stream': sys.stdout,
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'filters': ['require_debug_false']
            }
    },
    # This is the logger you use e.g. logging.getLogger(django)
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'project_logger': {
            'handlers': ['console', 'file', 'development_logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'test_logger': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
