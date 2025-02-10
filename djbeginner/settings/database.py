from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':  'mydatabase',
        'USER': 'postgres', 
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}