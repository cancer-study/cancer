# francistown.cancer gunicorn.conf
import os

from pathlib import Path

SOURCE_ROOT = str(Path(os.path.dirname(os.path.abspath(__file__))).parent)

errorlog = os.path.join(SOURCE_ROOT, 'log/cancer-gunicorn-error.log')
accesslog = os.path.join(SOURCE_ROOT, 'log/cancer-gunicorn-access.log')
loglevel = 'debug'
pidfile = os.path.join(SOURCE_ROOT, 'run/cancer-francistown.pid')

workers = 2  # the number of recommended workers is '2 * number of CPUs + 1'

raw_env = [f'DJANGO_SETTINGS_MODULE=cancer.settings.live.francistown']

bind = "127.0.0.1:9060"
