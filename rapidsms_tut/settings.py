# Django settings for rapidsms_tut project.

import os

# The top directory for this project. Contains requirements/, manage.py,
# and README.md, a rapidsms_tut directory with settings etc (see
# PROJECT_PATH), as well as a directory for each Django app added to this
# project.
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# The directory with this project's templates, settings, urls, static dir,
# wsgi.py, fixtures, etc.
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'rapidsms_tut')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {  ## (this will be overridden below by Salt)
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'rapidsms_tut.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/public/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/public/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files to collect
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'etpdbob1$x3(pqdhb6xn86^o9hzb=n#&27oeh^k(($0&7m2ii@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'rapidsms_tut.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'rapidsms_tut.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)

# A sample logging configuration.
# This logs all rapidsms messages to the file `/var/log/rapidsms_tut/rapidsms.log`
LOG_FILE_NAME = '/var/log/rapidsms_tut/rapidsms.log'
# It also sends an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'basic',
            'filename': LOG_FILE_NAME,
        },

    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'rapidsms': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rtropo.views': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'textit.views': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propigate': True,
        },
        'textit.outgoing': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propigate': True,
        }
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # External apps
    "django_nose",
    #"djtables",  # required by rapidsms.contrib.locations
    "django_tables2",
    "selectable",
    "south",
    'tut',
    # RapidSMS
    "rapidsms",
    "voting",
    "rtropo",
    'rapidsms_textit',
    "rapidsms.backends.database",
    "rapidsms.contrib.handlers",
    "rapidsms.contrib.httptester",
    "rapidsms.contrib.messagelog",
    "rapidsms.contrib.messaging",
    "rapidsms.contrib.registration",
    "rapidsms.contrib.echo",
    "rapidsms.contrib.default",  # Must be last
)

INSTALLED_BACKENDS = {
    "message_tester": {
        "ENGINE": "rapidsms.backends.database.DatabaseBackend",
    },
    "my-tropo-backend": {
        "ENGINE": "rtropo.outgoing.TropoBackend",
        'config': {
            # Your Tropo application's outbound token for messaging
            'messaging_token': '9ef79b49d3bb2e46a20abfa1209c6d0066b5764fb306e2abf2b6fde37ac25922733d988c8f7f0958271f8eaf',
            # Your Tropo application's voice/messaging phone number (including country code)
            'number': '+1-307-201-3499',
        },
    },
    'test-textit-backend': {
        'ENGINE': 'rapidsms_textit.outgoing.TextItBackend',
        'config': {
            "api_token": "de78a27456b82f8876e48d7ef339f75a1a6cfbd2",
            "number": "+2348099890451",
            "query_key": "key=MumbleMumble"  # this string must be sent as part of the URL from text.it
            # define our webhook URL like: http://vern-test.digvil.org/test_textit/?key=MumbleMumble
        },
    }
}

LOGIN_REDIRECT_URL = '/'

RAPIDSMS_HANDLERS = (
    'rapidsms.contrib.echo.handlers.echo.EchoHandler',
    # 'rapidsms.contrib.echo.handlers.ping.PingHandler',
    'voting.handlers.ResultsHandler',
    'voting.handlers.VoteHandler',
)
