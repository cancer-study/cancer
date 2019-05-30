"""
Django settings for cancer project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os
import sys


from django.core.management.color import color_style

from .logging import LOGGING
from .sites import get_site_id


style = color_style()

APP_NAME = 'cancer'

REVIEWER_SITE_ID = 1

MYSQL_DIR = os.path.join('/etc', APP_NAME, 'mysql.conf')

LOGIN_REDIRECT_URL = 'home_url'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ETC_DIR = '/etc'
# ETC_DIR = os.path.join(str(PurePath(BASE_DIR).parent), 'etc')

LOGIN_REDIRECT_URL = 'home_url'

SITE_ID = get_site_id('gaborone')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if not DEBUG:

    ETC_DIR = os.path.join('/etc', APP_NAME, 'live')

    LIVE_SYSTEM = 'LIVE'
    KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')
    AUTO_CREATE_KEYS = False

    with open(os.path.join(ETC_DIR, 'secret_key')) as f:
        SECRET_KEY = f.read().strip()

    MYSQL_DIR = os.path.join('/etc', APP_NAME, 'live')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': os.path.join(MYSQL_DIR, 'mysql.conf'),
            },
        },
    }

    INDEX_PAGE = 'https://cancer-live.bhp.org.bw'

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'unix:/tmp/memcached.sock',
        }
    }
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

    STATIC_ROOT = os.path.expanduser('~/static/live/')
    STATIC_URL = os.path.expanduser('/static/')
else:
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.10/howto/static-files/
    STATIC_ROOT = 'static'
    STATIC_URL = '/static/'

    MEDIA_ROOT = 'media'
    MEDIA_URL = '/media/'
    INDEX_PAGE = 'localhost:8000'

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '2^p0phb&x&ntbsduf6afw(@efi(+!&hm_lrjr-+$5v(t0_f+6t'
    # Database
    # https://docs.djangoproject.com/en/1.10/ref/settings/#databases

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': os.path.join(ETC_DIR, f'{APP_NAME}', 'mysql.conf'),
            },
        },
    }


ALLOWED_HOSTS = ['cancer-live.bhp.org.bw', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'django_extensions',
    'simple_history',
    'corsheaders',
    'rest_framework',
    'django_js_reverse',
    'rest_framework.authtoken',
    'edc_model_admin.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_offstudy.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_form_validators.apps.AppConfig',
    'edc_fieldsets.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_lab_dashboard.apps.AppConfig',
    'edc_list_data.apps.AppConfig',
    'edc_sync.apps.AppConfig',
    'edc_sync_files.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_label.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'cancer_dashboard.apps.AppConfig',
    'cancer_metadata_rules.apps.AppConfig',
    'cancer_reference.apps.AppConfig',
    'cancer.apps.EdcLocatorAppConfig',
    'cancer.apps.EdcTimepointAppConfig',
    'cancer.apps.EdcAppointmentAppConfig',
    'cancer.apps.EdcBaseAppConfig',
    'cancer.apps.EdcDeviceAppConfig',
    'cancer.apps.EdcIdentifierAppConfig',
    'cancer.apps.EdcLabAppConfig',
    'cancer.apps.EdcMetadataAppConfig',
    'cancer.apps.EdcProtocolAppConfig',
    'cancer.apps.EdcVisitTrackingAppConfig',
    'cancer.apps.EdcFacilityAppConfig',
    'cancer_subject.apps.AppConfig',
    'cancer_subject_validations.apps.AppConfig',
    'cancer_visit_schedule.apps.AppConfig',
    'cancer_prn.apps.AppConfig',
    'cancer.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
    'edc_lab_dashboard.middleware.DashboardMiddleware'
]

ROOT_URLCONF = 'cancer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = f'{APP_NAME}.wsgi.application'


if 'test' in sys.argv and 'mysql' not in DATABASES.get('default').get('ENGINE'):
    MIGRATION_MODULES = {
        "django_crypto_fields": None,
        "edc_call_manager": None,
        "edc_appointment": None,
        "edc_call_manager": None,
        "edc_consent": None,
        "edc_death_report": None,
        "edc_export": None,
        "edc_identifier": None,
        "edc_lab": None,
        "edc_metadata": None,
        "edc_rule_groups": None,
        "edc_registration": None,
        "edc_sync_files": None,
        "edc_sync": None,
        "cancer_subject": None}

if 'test' in sys.argv:
    PASSWORD_HASHERS = ('django_plainpasswordhasher.PlainPasswordHasher',)
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'))

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

USE_TZ = True


GIT_DIR = BASE_DIR
DEVICE_ID = '99'
DEVICE_ROLE = 'CentralServer'
LABEL_PRINTER = 'label_printer'

EDC_LAB_REQUISITION_MODEL = 'cancer_subject.subjectrequisition'
DEFAULT_APPOINTMENT_MODEL = 'cancer_subject.appointment'
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'PAGE_SIZE': 1,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.LimitOffsetPagination',
    )
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

COUNTRY = 'botswana'
HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')

EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USB_VOLUME = None
EDC_SYNC_SERVER_IP = None

MAIN_NAVBAR_NAME = APP_NAME

CUPS_SERVERS = {
    'localhost': None}

# dashboards
DASHBOARD_URL_NAMES = {
    'subject_models_url': 'subject_models_url',
    'subject_listboard_url': 'cancer_dashboard:subject_listboard_url',
    'screening_listboard_url': 'cancer_dashboard:screening_listboard_url',
    'subject_dashboard_url': 'cancer_dashboard:subject_dashboard_url',
}

LAB_DASHBOARD_URL_NAMES = {}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'cancer/base.html',
    'dashboard_base_template': 'cancer/base.html',
    'screening_listboard_template': 'cancer_dashboard/screening/listboard.html',
    'subject_listboard_template': 'cancer_dashboard/subject/listboard.html',
    'subject_dashboard_template': 'cancer_dashboard/subject/dashboard.html',
}

SITE_ID = '040'
SITE_IDS = ['040', '060']
REVIEWER_SITE_ID = '1'
PARENT_REFERENCE_MODEL1 = None
PARENT_REFERENCE_MODEL2 = None
