from ...sites import get_site_id
from .base_live import *

# for django.contrib.sites
SITE_ID = get_site_id('francistown')

WSGI_APPLICATION = 'cancer.wsgi.francistown.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'cancer-live.bhp.org.bw',
    'francistown.cancer.bhp.org.bw']
