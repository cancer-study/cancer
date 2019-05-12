# uat.cancer gunicorn.conf
import os

from pathlib import Path

SOURCE_ROOT = str(Path(os.path.dirname(os.path.abspath(__file__))).parent)

errorlog = os.path.join(
    SOURCE_ROOT, 'log/cancer-uat-gaborone-gunicorn-error.log')
accesslog = os.path.join(
    SOURCE_ROOT, 'log/cancer-uat-gaborone-gunicorn-access.log')
loglevel = 'debug'
pidfile = os.path.join(SOURCE_ROOT, 'run/cancer-uat-gaborone.pid')

workers = 2  # the number of recommended workers is '2 * number of CPUs + 1'

raw_env = ['DJANGO_SETTINGS_MODULE=cancer.settings.test.gaborone-uat']

bind = "127.0.0.1:9110"
