"""
WSGI config for honda project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys


sys.path.append('/home/django/domains/honda/honda/honda/')
sys.path.append('/home/django/domains/honda/lib/python2.7/site-packages/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "honda.settings")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "honda.settings")

application = get_wsgi_application()