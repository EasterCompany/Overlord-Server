import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY_FILE = open('./.secret')
SECRET_KEY = SECRET_KEY_FILE.read()
SECRET_KEY_FILE.close()
DEBUG = True

ALLOWED_HOSTS = [
    # Development
    '.localhost',
    # Production
    '.easter.company'
]

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # Easter Apps
    'api',
    'core'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'djdev_panel.middleware.DebugMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'clients', 'Templates'),
            os.path.join(BASE_DIR, 'clients', 'Chat', 'build'),
            os.path.join(BASE_DIR, 'clients', 'Global', 'build'),
            os.path.join(BASE_DIR, 'clients', 'Journal', 'build'),
            os.path.join(BASE_DIR, 'clients', 'Finance', 'build'),
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

WSGI_APPLICATION = 'web.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'clients', 'Chat', 'build', 'static'),
    os.path.join(BASE_DIR, 'clients', 'Finance', 'build', 'static'),
    os.path.join(BASE_DIR, 'clients', 'Global', 'build', 'static'),
    os.path.join(BASE_DIR, 'clients', 'Journal', 'build', 'static'),
)

# Solves cors issue while serving React Apps
# https://blog.usejournal.com/serving-react-and-django-together-2089645046e4
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://localhost:8100'
)

# Adds media upload path
# https://www.geeksforgeeks.org/python-uploading-images-in-django/
MEDIA_URL = '/data/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'data')
