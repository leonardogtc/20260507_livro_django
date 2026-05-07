from .settings import *

DEBUG = True

SECRET_KEY = ')fa^h1vv=_f-jx&z-x2w7x_@u_ci_%z+eqx$_8o0w6$0m4h16f'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}