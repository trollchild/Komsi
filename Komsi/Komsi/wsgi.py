"""
WSGI config for Raksire project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append("/home/admin/Komsi/Komsi/")

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'Komsi.settings'

application = get_wsgi_application()
