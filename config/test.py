from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'TEST': {
            "NAME": "catalogue_test"
        }
    }
}

TEST_DISCOVER_TOP_LEVEL = os.path.join(BASE_DIR, 'catalogue'),
TEST_DISCOVERY_ROOT = os.path.join(BASE_DIR, 'catalogue'),
TEST_DISCOVER_PATTERN = "test_*"
