from ...sites import get_site_id
from .base_live import *

# for django.contrib.sites
SITE_ID = get_site_id('gaborone')

WSGI_APPLICATION = 'cancer.wsgi.gaborone.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'cancer-live.bhp.org.bw',
    'gaborone.cancer.bhp.org.bw']
