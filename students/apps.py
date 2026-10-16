# apps.py файл конфигурации приложений (Django автоматически создаёт классы предоставлящие приложение)
from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = 'students'
