# admin.py модуль управлчет данными через встроенный инструмент Django
from django.contrib import admin



# Вариант 1 регистрация модели
# from .models import Student
#
# admin.site.register(Student)



# Вариант 2 регистрация модели и более гибкий
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'year',)
    list_filter = ('year',)                       # фильтрация
    search_fields = ('first_name', 'last_name',)   # строка поиска по нескольким полям
