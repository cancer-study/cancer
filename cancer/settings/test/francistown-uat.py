from .base_test import *

# site is francistown
SITE_ID = 70

WSGI_APPLICATION = 'cancer.wsgi.francistown-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'francistown.uat.cancer.bhp.org.bw']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'uat.conf'),
        },
    },
}
