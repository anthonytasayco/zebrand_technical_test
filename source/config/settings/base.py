import environ

BASE_DIR = environ.Path(__file__) - 3
env = environ.Env()
env.read_env(env.str('ENV_PATH', BASE_DIR('.env')))

DEBUG = env.get_value('DEBUG', bool, True)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'drf_yasg',
]

LOCAL_APPS = [
    'apps.products',
    'apps.users',
    'apps.web',
]

INSTALLED_APPS = \
    DJANGO_APPS + \
    THIRD_PARTY_APPS + \
    LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGE_CODE = 'es-mx'

STATIC_ROOT = str(BASE_DIR('staticfiles'))

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    str(BASE_DIR.path('static')),
]


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


AUTH_USER_MODEL = 'users.User'

ADMIN_URL = 'admin'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    "PAGE_SIZE": 20,
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str('POSTGRES_PORT', '5432'),
    }
}

ENABLE_API_DOCUMENTATION = env.get_value('ENABLE_API_DOCUMENTATION', bool, True)
EMAIL_HOST = env.get_value('EMAIL_HOST', str, 'smtp-server')
EMAIL_PORT = env.get_value('EMAIL_PORT', str, '1025')

REDIS_URL = env.get_value('REDIS_URL', str, 'redis://redis:6379/0')

BROKER_URL = 'redis://redis:6379/0'
CELERY_BROKER_URL = "redis://redis:6379/0"