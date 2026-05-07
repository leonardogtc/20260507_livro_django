from .settings import *

DEBUG = True

SECRET_KEY = ')0=uget%k*5w%v=!!)o2zqvtod#34)j08mo2-^5d^5*vjl*d-7'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}