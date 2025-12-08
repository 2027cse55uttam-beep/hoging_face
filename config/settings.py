import os
import dj_database_url
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CKEditor Settings
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# Default Local Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Agar Render par hain, to wahan ka database use karo
database_url = os.environ.get("DATABASE_URL")
if database_url:
    DATABASES['default'] = dj_database_url.parse(database_url)


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/
STATIC_URL = 'static/'
# Ye zaroori hai taaki Render saari CSS files ek jagah jama kar sake
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# WhiteNoise Storage (Compression ke liye)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# PRODUCTION SECURITY SETTINGS

# 1. HSTS: Browser ko bolo ki agle 1 saal tak sirf HTTPS use kare
SECURE_HSTS_SECONDS = 31536000  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# 2. SSL Redirect: Agar koi http:// khole toh auto https:// kar do
SECURE_SSL_REDIRECT = True

# 3. Cookies Secure: Cookies tabhi bhejo jab connection secure ho
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# 4. XSS Protection: Browser ko bolo script attacks block kare
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# 5. Render Specific (CSRF Fix) - IMPORTANT
# Render ka URL yahan dalna zaroori hai warna Forms submit nahi honge
CSRF_TRUSTED_ORIGINS = ['https://hoging-face.onrender.com']

X_FRAME_OPTIONS = 'DENY'

# JAZZMIN SETTINGS (Dashboard Design)
JAZZMIN_SETTINGS = {
    "site_title": "RoyFolio Admin",
    "site_header": "RoyFolio Dashboard",
    "site_brand": "RoyFolio",
    "welcome_sign": "Welcome back, Admin!",
    "copyright": "RoyFolio Ltd",
    "search_model": "core.Project", # Top search bar projects search karega
    
    # Side Menu Icons (FontAwesome)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "core.Project": "fas fa-laptop-code",  # Project ke liye Laptop icon
        "core.Contact": "fas fa-envelope-open-text", # Contact ke liye Email icon
    },
    
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs", # Forms tabs mein dikhenge
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",   # Clean Modern Look
    "dark_mode_theme": "darkly", # Dark mode support
}