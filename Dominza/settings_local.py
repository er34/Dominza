# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#SESSION_ENGINE="django.contrib.sessions.backends.cache"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dominzadb',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'www',
        'PASSWORD': '82jvlauhG21'
    }
}
