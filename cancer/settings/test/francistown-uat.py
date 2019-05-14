from .base_test import *

# site is francistown
SITE_ID = 60

WSGI_APPLICATION = 'cancer.wsgi.francistown-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'cancer-live.bhp.org.bw',
    'francistown.uat.cancer.bhp.org.bw']