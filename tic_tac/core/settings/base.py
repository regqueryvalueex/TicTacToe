"""
Django settings for profit_reporter light_it.

Generated by 'django-admin startlight_it' using Django 1.8.

For more information on this file, see
https://docs.djangolight_it.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangolight_it.com/en/1.8/ref/settings/
"""

# Build paths inside the light_it like this: os.path.join(BASE_DIR, ...)
import os

WEBSITE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
PROJECT_ROOT = os.path.abspath(os.path.dirname(WEBSITE_ROOT))

# Quick-start development settings - unsuitable for production
# See https://docs.djangolight_it.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rR7<{p^SAdu%>pGaDPXkld^5gv~ckHa+R3{eTmmDPXQB!=T1VuVzO!&j1a<ab7KyX!_2<+BPpX?'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third-party packages
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_nose',
    'channels',

    # internal packages
    'api',
    'accounts',
    'games',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SOCIALACCOUNT_PROVIDERS = {
     'google':
         {
             'SCOPE': ['profile', 'email'],
         }
     }

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_ADAPTER = "accounts.adapters.AccountAdapter"

ROOT_URLCONF = 'core.urls'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(WEBSITE_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangolight_it.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'light_it_db.db',
        # 'USER': 'light_it_usr',
        # 'PASSWORD': 'kdyr;s74,bdr',
        # 'HOST': 'localhost',
        # 'PORT': 5432
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "tic_tac.core.routing.channel_routing",
    },
}

# Internationalization
# https://docs.djangolight_it.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangolight_it.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media_root')


STATICFILES_DIRS = (
    ('vendor', os.path.join(PROJECT_ROOT, 'static', 'bower_components')),
    ('js', os.path.join(PROJECT_ROOT, 'static', 'js')),
    ('css', os.path.join(PROJECT_ROOT, 'static', 'css')),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.MultiPartRenderer',
    ),
}

AUTH_USER_MODEL = 'accounts.User'

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]