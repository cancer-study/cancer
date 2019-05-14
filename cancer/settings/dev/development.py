# Settings for development, e.g. tests, runserver

import os
import sys

from ..base import *

DEBUG = True

ETC_DIR = os.path.join(BASE_DIR, 'etc')

MYSQL_DIR = ETC_DIR

WSGI_APPLICATION = 'cancer.wsgi.wsgi.application'

ALLOWED_HOSTS = ['localhost', '192.168.157.7']

SECRET_KEY = '614!=u17sy1x__5psj(7*-q61tc@j-gn5$&+_-sy@psn*4wn&!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'cancer',
        'USER': 'root',
        'PASSWORD': 'thabokga@321',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

SITE_ID = 40

INDEX_PAGE = 'localhost:8000'

STATIC_ROOT = os.path.join(BASE_DIR, APP_NAME, 'static')

CUPS_SERVERS = {
    'bhp.printers.bhp.org.bw': 'bhp.printers.bhp.org.bw',
    'cancer-test.bhp.org.bw': 'cancer-test.bhp.org.bw',
    'localhost': None}

if 'test' in sys.argv:

    class DisableMigrations:

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher', )
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
