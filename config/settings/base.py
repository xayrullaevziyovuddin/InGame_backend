import sys
from pathlib import Path
import environ

# -------------------------------
# 1. Базовые настройки пути
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Добавляем директорию apps в sys.path, если используется папка "apps" для локальных приложений
sys.path.append(str(BASE_DIR / "apps"))

# -------------------------------
# 2. Чтение переменных из .env
# -------------------------------

env = environ.Env(
    DEBUG=(bool, False)  # По умолчанию DEBUG=False
)
environ.Env.read_env(str(BASE_DIR / ".env"))  # Читаем переменные окружения

# -------------------------------
# 3. Основные настройки
# -------------------------------

DEBUG = env.bool("DEBUG", default=False)

SECRET_KEY = env.str("SECRET_KEY", default=None)
if not SECRET_KEY:
    raise ValueError("SECRET_KEY не задан в .env!")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

# -------------------------------
# 4. Установленные приложения
# -------------------------------

BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",  # Django REST framework
    "django_filters",  # Фильтрация API-запросов
    "corsheaders",  # CORS (если фронтенд на отдельном сервере)
    "drf_yasg",  # Swagger UI, и ReDoc
]

LOCAL_APPS = [
    "products",
    "orders",
    "comments",
    "news",
    "services",
]

INSTALLED_APPS = BASE_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# -------------------------------
# 5. Middleware
# -------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # CORS
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------------------------------
# 6. Настройки URL и WSGI
# -------------------------------

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

# -------------------------------
# 7. Шаблоны
# -------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------------------------------
# 8. База данных
# -------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # Файл базы данных будет находиться в корне проекта
    }
}

# -------------------------------
# 9. Валидаторы паролей
# -------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------------
# 10. Локализация
# -------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True

# -------------------------------
# 11. Статические и медиа-файлы
# -------------------------------

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------------
# 12. CORS (если фронтенд на другом сервере)
# -------------------------------

CORS_ALLOW_ALL_ORIGINS = True  # Разрешить все запросы (для разработки)
# CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=["http://localhost:3000"])

# -------------------------------
# 13. Django REST Framework (DRF)
# -------------------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ]
}

# -------------------------------
# 14. ID полей моделей
# -------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
