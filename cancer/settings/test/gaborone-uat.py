from .base_test import *

# site is gaborone
SITE_ID = 40

WSGI_APPLICATION = 'cancer.wsgi.gaborone-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'cancer-live.bhp.org.bw',
    'gaborone.uat.cancer.bhp.org.bw']

TIME_ZONE = 'Africa/Gaborone'
