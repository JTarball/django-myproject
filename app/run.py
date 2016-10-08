#!/usr/bin/env python
"""
    run.py
    ======
    This is the main run script for running a
     Django Server in PRODUCTION.

    WSGI config for docker_django project.
    It exposes the WSGI callable as a module-level variable named ``application``.
    For more information on this file, see
    https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import os

import eventlet

from django.core.wsgi import get_wsgi_application

from eventlet import wsgi
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.base")
application = get_wsgi_application()
application = DjangoWhiteNoise(application)

if __name__ == '__main__':
    print 'Serving on 8000...'
    wsgi.server(eventlet.listen(('', 8000)), application)
