import os

SOURCE_ROOT = os.path.expanduser('~/source')
APP_NAME = 'cancer'

bind = "127.0.0.1:9000"
errorlog = os.path.join(SOURCE_ROOT, f'{APP_NAME}/logs/gunicorn-error.log')
accesslog = os.path.join(SOURCE_ROOT, f'{APP_NAME}/logs/gunicorn-access.log')
loglevel = 'debug'
workers = 2
