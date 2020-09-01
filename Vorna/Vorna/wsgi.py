"""
WSGI config for Vorna project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Vorna')
sys.path.append('C:/Vorna/Vorna')

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Vorna.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Vorna.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Vorna.settings")

application = get_wsgi_application()
