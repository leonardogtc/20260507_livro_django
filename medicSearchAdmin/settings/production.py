from .settings import *

DEBUG = True

SECRET_KEY = 'at@ua*xkyeu24sy8#pl0ngr(=hrc$^%n2m0d@6z+y@hkjxnpl^'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}