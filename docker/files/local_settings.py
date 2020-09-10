# Django settings for patchman project.

import os

DEBUG = False

ADMINS = (
    ('Admin Name', 'admin@example.com'),
)

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'patchman',
       'USER': 'patchman',
       'PASSWORD': 'password',
       'HOST': 'patchman.c488z2dafhwr.us-east-1.rds.amazonaws.com',
       'PORT': '3306',
       'STORAGE_ENGINE': 'INNODB',
       'CHARSET': 'utf8'
   }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# Create a unique string here, and don't share it with anybody.
SECRET_KEY = 'PLEASE_CHANGE_ME_TO_UNIQUE_SECURE_SECRET_KEY'

# Add the IP addresses that your web server will be listening on,
# instead of '*'
ALLOWED_HOSTS = ['127.0.0.1', '*']

# Maximum number of mirrors to add or refresh per repo
MAX_MIRRORS = 5

# Number of days to wait before notifying users that a host has not reported
DAYS_WITHOUT_REPORT = 14

# Whether to run patchman under the gunicorn web server
RUN_GUNICORN = False

# Enable memcached
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}