from pathlib import Path
import os
from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

include(
    'components/installed_apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/database.py',
    'components/auth_password_validators.py'
)

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOWED_HOSTS = ['127.0.0.1']

LOCALE_PATHS = ['movies/locale']
