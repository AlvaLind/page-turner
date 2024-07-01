from pathlib import Path
from page_turner.settings import *
import os
import sys
import dj_database_url
from django.contrib.messages import constants as messages

# Fetch base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from env.py 
if os.path.isfile('env.py'):
    import env

# Middleware
MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Use SQLite for testing
if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
