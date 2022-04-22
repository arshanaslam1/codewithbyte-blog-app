"""
WSGI config for Online_Portfolio_and_Blog_With_CMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Online_Portfolio_and_Blog_With_CMS.settings')

application = get_wsgi_application()
