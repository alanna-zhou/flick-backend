"""
Django settings for flick project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from decouple import config

TMDB_API_KEY = config("TMDB_API_KEY")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMP_DIR = "tmp"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

DEBUG = int(config("DEBUG", default=0))


VALIDATE_SOCIAL_TOKEN = False
# URL for validate Facebook Token
VALIDATE_FACEBOOK_TOKEN_URL = "https://graph.facebook.com/me"

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS").split(" ")

TEST_RUNNER = "django_slowtests.testrunner.DiscoverSlowestTestsRunner"
NUM_SLOW_TESTS = 10

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # third party
    "celery",
    "django_celery_beat",
    "django_celery_results",
    "friendship",
    "rest_framework",
    "rest_framework.authtoken",
    # own
    "api",
    "asset",
    "cast",
    "comment",
    "flick_auth",
    "friend",
    "item",
    "lst",
    "like",
    "member",
    "notification",
    "pages",
    "rating",
    "search",
    "show",
    "tag",
    "user",
]

# needed to test in Postman
REST_FRAMEWORK = {"DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework.authentication.TokenAuthentication"]}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "flick.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
)

WSGI_APPLICATION = "flick.wsgi.application"

CACHES = {
    "default": {
        "BACKEND": "lrucache_backend.LRUObjectCache",
        "TIMEOUT": 600,
        "OPTIONS": {"MAX_ENTRIES": 100, "CULL_FREQUENCY": 100},
        "NAME": "optional-name",
    },
    "local": {
        "BACKEND": "lrucache_backend.LRUObjectCache",
        "TIMEOUT": 600,
        "OPTIONS": {"MAX_ENTRIES": 100, "CULL_FREQUENCY": 100},
        "NAME": "optional-name",
    },
}


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# For MySQL:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': '80',
#     }
# }

if DEBUG:
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": os.path.join(BASE_DIR, "db.sqlite3")}}
else:
    DATABASES = {
        "default": {
            "ENGINE": config("SQL_ENGINE", "django.db.backends.sqlite3"),
            "NAME": config("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": config("SQL_USER", "user"),
            "PASSWORD": config("SQL_PASSWORD", "password"),
            "HOST": config("SQL_HOST", "localhost"),
            "PORT": config("SQL_PORT", "5432"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

# S3 (for images)
S3_BUCKET = "flick"
S3_BASE_URL = f"https://{S3_BUCKET}.s3-us-west-1.amazonaws.com/"

# MovieDB setup
TMDB_BASE_URL = "http://image.tmdb.org/t/p/w185"

# Celery
"""
Common Docker image issues:
1. use redis address in the comments below when if using `docker-compose build`
2. your local redis port is already running, use `npx kill-port 6379` to kill it
"""
CELERY_BROKER_URL = "redis://localhost:6379"  # "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"  # "redis://redis:6379/0"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
