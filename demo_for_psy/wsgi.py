"""
WSGI config for demo_for_psy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from demo_for_psy.asgi import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_for_psy.settings')

app = application
