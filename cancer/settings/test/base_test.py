import os

from ..logging import LOGGING
from ..base import *

DEBUG = False

# WARNING_MESSAGE = 'This is a test system. Do not use for production data collection! '

ETC_DIR = os.path.join('/etc', APP_NAME, 'uat')


KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')
AUTO_CREATE_KEYS = False

SECRET_KEY = '2^p0phb&x&ntbsduf6afw(@efi(+!&hm_lrjr-+$5v(t0_f+6t'

MYSQL_DIR = os.path.join('/etc', APP_NAME, 'uat')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'mysql.conf'),
        },
    },
}



INDEX_PAGE = 'https://cancer-live.bhp.org.bw'

CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

STATIC_ROOT = '/var/www/cancer/test/static'

# edc_sync / sync files
EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None
