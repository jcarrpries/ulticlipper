SECRET_KEY = 'django-insecure-@50(tinlxmb)6ir0*1841a5@c$p+ai&2#jpaohbt(-_hri_pct'

DEBUG = False

ALLOWED_HOSTS = ['.localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'backend',
        'USER': 'backend',
        'PASSWORD': 'good_password',
        'HOST': 'ulticlipper-database-ci',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
