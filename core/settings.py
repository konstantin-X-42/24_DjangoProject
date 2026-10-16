import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(override=True)

# путь до текущего приложения (для построения абсолютных путей до статистических файлов)
BASE_DIR = Path(__file__).resolve().parent.parent


# секретный криптографический ключ для подписей (выносить в переменное окружение не загружается в репозиторий)
SECRET_KEY = os.getenv('SECRET_KEY')  # передаём значение ключа из файла .env



# режим отладки (следить за приложением отслеживать ошибки, после внесения изменений перезагружает сервер)
DEBUG = True if os.getenv('DEBUG') == "True" else False     # передаём значение True из файла .env

# список доменных имен обслуживаемые нашим приложением
ALLOWED_HOSTS = []


# список приложений (сюда будем добовлять свои приложения)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'students'
]

# список приложений доставляющих промежуточное ПО, обрабатывающие входящие зпросы и исходящие ответы
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# путь до модуля с маршрутами core/urls
ROOT_URLCONF = 'core.urls'

# настройки шаблонизации, директории шаблонов и контекстные процессы
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

# путь к wsgi-приложениям (точка входа для совместимости с wsgi серверами)
WSGI_APPLICATION = 'core.wsgi.application'


# настройка для подключения к базе данных дефолтное указано sqlite3 (можно подключить посгрес, оракол или майэскуэль)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # меняем на postgresql_psycopg2
        'NAME': os.getenv('NAME') ,                         # указываем имя нашей базы данных
        'USER': os.getenv('USER') ,                         # указываем пользователя
        'PASSWORD': os.getenv('PASSWORD') ,                 # указываем пароль
        'HOST': os.getenv('HOST') ,                         # указываем хост (база данных у нас локально)
        'PORT': os.getenv('PORT') ,                         # указываем порт для подключения базы postgresql
    }
}


# список валидаторов (используются для проверки надёжности паролей пользователей)
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


# язык для проекта
LANGUAGE_CODE = 'en-us'

# часовая зона для проекта по дефолту - UTC. устанавливаем 'Europe/Moscow'
TIME_ZONE = 'Europe/Moscow'

# включает поддержку интернационализации
USE_I18N = True

# настройка включает поддержку локализации (дописали сами)
USE_L10N = True

# в django необходимо включить поддержку временных зон
USE_TZ = True


# маршрут до доступа к нашей статике
STATIC_URL = 'static/'

# список директорий на диске из которых будут подгружаться статические файлы (STATICFILES_DIRS = [BASE_DIR / 'static'] дописали самостоятельно)
STATICFILES_DIRS = [BASE_DIR / 'static']

# маршрут для доступа к медиа файлам (MEDIA_URL = '/media/' дописали самостоятельно)
MEDIA_URL = '/media/'

# директория (путь) на диске где будут храниться медиа файлы загружаемые пользователями (MEDIA_ROOT = BASE_DIR / 'media' дописали самостоятельно)
MEDIA_ROOT = BASE_DIR / 'media'

# настроцка уазывает первичный ключ для реализованных моделей которые будут взаимодействовать с базой данных (в уроке есть у меня нет дописал самостоятельно)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Email
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}
