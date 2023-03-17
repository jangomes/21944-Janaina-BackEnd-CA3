from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': BASE_DIR / 'db_dev.mysql',}}
