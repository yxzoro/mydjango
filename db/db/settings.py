import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '2q3bqr@@7htj8mje!k8be#bj%nxu&ftk6y$l4ei)!&kmk%w!xz'

INSTALLED_APPS = ('db', )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


