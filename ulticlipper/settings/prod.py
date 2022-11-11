import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ["ulticlipper.jessmuir.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'backend',
        'USER': 'backend',
        'PASSWORD': 'good_password',
        'HOST': 'ulticlipper-database-prod',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
