"""
WSGI config for page_turner.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'page_turner.settings')

application = get_wsgi_application()
