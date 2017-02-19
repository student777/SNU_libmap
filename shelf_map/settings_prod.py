from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shelf_map',
        'USER': 'postgres',
        'PASSWORD': '1234',
    }
}
